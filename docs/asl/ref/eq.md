
Query expression that matches time series where the value for a given key is an exact
match for the provided value. Suppose you have three time series:

* `name=http.requests, status=200, nf.app=server`
* `name=http.requests, status=400, nf.app=server`
* `name=sys.cpu, type=user, nf.app=server`

The query `name,http.requests,:eq` would be equivalent to an infix query like
`name = http.requests` and would match:

* `name=http.requests, status=200, nf.app=server`
* `name=http.requests, status=400, nf.app=server`