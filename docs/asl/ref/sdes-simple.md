@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Apply sliding double exponential smoothing using simple default parameters. This is a convenience
operator that provides deterministic DES functionality with reasonable defaults, offering better
stability than the standard [:des-simple](des-simple.md) operator.

## Parameters

* **expr**: The time series expression to apply sliding double exponential smoothing to

## Default Configuration

This operator is equivalent to calling `:sdes` with these default parameters:

- **Training**: 10 data points
- **Alpha**: 0.1 (level smoothing factor)
- **Beta**: 0.5 (trend smoothing factor)

## Equivalent Expression

This convenience operator is shorthand for:

```asl
# These expressions are equivalent:
name,cpu,:eq,:sum,:sdes-simple
name,cpu,:eq,:sum,:dup,10,0.1,0.5,:sdes
```

## Examples

Basic sliding DES smoothing with default parameters:

@@@ atlas-example { hilite=:sdes-simple }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:sdes-simple
@@@

## Related Operations

* [:sdes](sdes.md) - Full sliding DES with custom parameters
* [:des-simple](des-simple.md) - Standard DES equivalent (less stable)
* [:des-fast](des-fast.md) - DES helper for quick adaptation
* [:sdes-fast](sdes-fast.md) - Sliding DES optimized for quick adaptation

## See Also

* [Double Exponential Smoothing](../des.md) - Complete DES documentation with parameter guidance
* [Sliding DES](sdes.md) - Detailed explanation of the sliding variant