@@@ atlas-signature
seed: Int
-->
TimeSeriesExpr
@@@

Generate a deterministic pseudo-random time series using a specified seed value. This creates
reproducible "random" data useful for experimentation, testing, and sample data generation.
Unlike [:random](random.md), this operator allows creating multiple distinct but reproducible
random sequences.

## Parameters

* **seed**: Integer seed value that determines the random sequence (different seeds produce different patterns)

## Behavior

* **Deterministic**: Same seed always produces identical output for the same time range
* **Hash-based**: Uses hash of timestamp combined with seed for randomness
* **Value range**: Each datapoint is between 0.0 and 1.0
* **Reproducible**: Multiple queries with same seed and time range produce identical results

## Examples

Creating a seeded random time series:

@@@ atlas-example { hilite=:srandom}
Seeded Random: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=42,:srandom
@@@

## Seed Selection

* **Different seeds**: Produce visually distinct random patterns
* **Consistent seeds**: Ensure reproducibility across sessions
* **Arbitrary values**: Any integer works as a seed (positive, negative, or zero)

## Comparison with :random

| Operator | Reproducibility | Multiple Sequences |
|----------|-----------------|-------------------|
| `:random` | Single deterministic sequence | No (always same pattern) |
| `:srandom` | **Seed-based deterministic** | **Yes (different seeds)** |

## Related Operations

* [:random](random.md) - Generate single deterministic pseudo-random sequence (no seed)
* [:const](const.md) - Generate constant values (opposite of random)
* [:time](time.md) - Generate time-based patterns
* [:add](add.md) / [:mul](mul.md) - Transform random values to different ranges
