
# and

There are two overloaded variants of the `:and` operator:

* [Query variant](#query-variant) that is used to help restrict the set of time series used
  for an expression.
* [Math variant](#math-variant) that is used to combine to signal time series.

## Query Variant

## Signature

`Query Query -- Query`

## Summary

Query expression that matches if both sub queries match. Suppose you have three time
series:

* `name=http.requests, status=200, nf.app=server`
* `name=sys.cpu, type=user, nf.app=foo`
* `name=sys.cpu, type=user, nf.app=bar`

The query `name,sys.cpu,:eq,nf.app,foo,:eq,:and` would match:

* `name=sys.cpu, type=user, nf.app=foo`

## Math Variant

## Signature

`TimeSeriesExpr TimeSeriesExpr -- TimeSeriesExpr`

## Summary

Compute a new time series where each interval has the value `(a AND b)` where `a`
 and `b` are the corresponding intervals in the input time series.
