@@@ atlas-signature
<empty>
-->
TimeSeriesExpr
@@@

Generate a time series that appears to be random noise for the purposes of
experimentation and generating sample data. To ensure that the line is deterministic
and reproducible it actually is based on a hash of the timestamp. Each datapoint is a
value between 0.0 and 1.0.

@@@ atlas-example { hilite=:random }
Random: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=:random
@@@