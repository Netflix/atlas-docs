@@@ atlas-signature
<empty>
-->
TimeSeriesExpr
@@@

Generate a deterministic pseudo-random time series for experimentation and sample data creation.
Each datapoint is a value between 0.0 and 1.0, generated using a hash-based function of the
timestamp to ensure reproducible results across multiple queries with the same time range.

## Output

* **Value range**: 0.0 to 1.0 (inclusive)
* **Deterministic**: Same time range always produces identical values
* **Distribution**: Approximately uniform across the range

## Examples

Basic random data generation:

@@@ atlas-example { hilite=:random }
Random: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=:random
@@@

## Related Operations

* [:const](const.md) - Generate constant values
* [:time](time.md) - Generate time-based patterns
* [:mul](mul.md) - Scale random values to different ranges
* [:add](add.md) - Shift random values to different base levels