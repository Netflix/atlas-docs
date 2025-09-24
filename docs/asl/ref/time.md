@@@ atlas-signature
mode: String
-->
TimeSeriesExpr
@@@

Generates a time series where each value corresponds to a component of the current time.
This is useful for creating time-based patterns, filters, and calculations.

## Parameters

* **mode**: A string specifying which time component to extract

## Supported Time Components

### Common Time Parts

* `secondOfMinute` - Second within the current minute (0-59)
* `minuteOfHour` - Minute within the current hour (0-59)
* `hourOfDay` - Hour within the current day (0-23)
* `dayOfWeek` - Day within the current week (1-7, Monday=1)
* `dayOfMonth` - Day within the current month (1-31)
* `monthOfYear` - Month within the current year (1-12)

### Extended Time Parts

* `secondOfDay` - Second within the current day (0-86399)
* `minuteOfDay` - Minute within the current day (0-1439)
* `dayOfYear` - Day within the current year (1-366)
* `yearOfCentury` - Year within the current century (0-99)
* `yearOfEra` - Year within the current era (e.g., 2024)

### Epoch-based Values

* `seconds` - Seconds since Unix epoch (1970-01-01)
* `days` - Days since Unix epoch

### Java ChronoField Enums

The mode can also be a value from the Java
[ChronoField](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/temporal/ChronoField.html)
enum (e.g., `HOUR_OF_DAY`, `MINUTE_OF_HOUR`).

## Examples

Hour of day using string mode:
@@@ atlas-example { hilite=:time }
/api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=hourOfDay,:time
@@@

Hour of day using Java enum:
@@@ atlas-example { hilite=:time }
/api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=HOUR_OF_DAY,:time
@@@

## Common Use Cases

* **Time-based filtering**: Select data only during business hours
* **Seasonal analysis**: Group data by day of week or month of year
* **Periodic patterns**: Create repeating patterns based on time cycles
* **Time comparisons**: Use in mathematical operations with other time series

## Related Operations

* [:offset](offset.md) - Shift time frame for fetching data
* [:const](const.md) - Generate constant values (compared to time-varying values)
* [:gt](gt.md), [:lt](lt.md) - Compare time values for filtering
* [:eq](eq.md) - Match specific time values