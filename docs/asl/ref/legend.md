@@@ atlas-signature
String
TimeSeriesExpr
-->
StyleExpr
@@@

Set the legend text. Legends can contain variables based on the
exact keys matched in the query clause and keys used in a
[group by](by.md). Variables start with a `$` sign and can optionally
be enclosed between parentheses. The parentheses are required for cases
where the characters immediately following the name could be a part
of the name. If a variable is not defined, then the name of the variable
will be used as the substitution value.

The variable `atlas.offset` can be used to indicate the [time shift](offset.md)
used for the underlying data.

Examples:

@@@ atlas-example { hilite=:legend }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by,$name,:legend
@@@

@@@ atlas-example { hilite=:legend }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,cluster+$nf.cluster,:legend
@@@