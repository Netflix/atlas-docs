@@@ atlas-signature
String
-->
TimeSeriesExpr
@@@

Generates a line based on the current time. Supported modes are:

* secondOfMinute
* secondOfDay
* minuteOfHour
* minuteOfDay
* hourOfDay
* dayOfWeek
* dayOfMonth
* dayOfYear
* monthOfYear
* yearOfCentury
* yearOfEra
* seconds (since epoch)
* days (since epoch)

The mode can also be a value of the enum
[ChronoField](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/temporal/ChronoField.html).

Examples:

@@@ atlas-example
Hour of Day: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=hourOfDay,:time
Enum: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=HOUR_OF_DAY,:time
@@@