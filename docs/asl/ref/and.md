
There are two variants of the `:and` operator.

## Choosing

This first variant is used for choosing the set of time series to operate on. It is
a binary operator that matches if both of the sub-queries match. Suppose you have
three time series:

* `name=http.requests, status=200, nf.app=server`
* `name=sys.cpu, type=user, nf.app=foo`
* `name=sys.cpu, type=user, nf.app=bar`

The query `name,sys.cpu,:eq,nf.app,foo,:eq,:and` would match:

* `name=sys.cpu, type=user, nf.app=foo`

## Math

Compute a new time series where each interval has the value `(a AND b)` where `a`
and `b` are the corresponding intervals in the input time series.