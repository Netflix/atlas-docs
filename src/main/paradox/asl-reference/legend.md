
# legend

## Signature

`TimeSeriesExpr String -- StyleExpr`

## Summary

Set the legend text. Legends can contain variables based on the
exact keys matched in the query clause and keys used in a
[group by](data-by). Variables start with a `$` sign and can optionally
be enclosed between parentheses. The parentheses are required for cases
where the characters immediately following the name could be a part
of the name. If a variable is not defined, then the name of the variable
will be used as the substitution value.

The variable `atlas.offset` can be used to indicate the [time shift](data-offset)
used for the underlying data.

There are also special variables that can be used to substitute the line statistics
into the legend text: `atlas.min`, `atlas.max`, `atlas.avg`, `atlas.last`, and `atlas.total`.

## Examples

### Simple

@@@ atlas-example
Before: /api/v1/graph?q=name,sps,:eq,(,name,),:by
 After: /api/v1/graph?q=name,sps,:eq,(,name,),:by,$name,:legend
@@@

### Variable with Additional Text

@@@ atlas-example
Before: /api/v1/graph?q=name,sps,:eq,(,nf.cluster,),:by
 After: /api/v1/graph?q=name,sps,:eq,(,nf.cluster,),:by,cluster+$nf.cluster,:legend
@@@

### Including Offset

@@@ atlas-example
Before: /api/v1/graph?q=name,sps,:eq,:sum,1w,:offset
 After: /api/v1/graph?q=name,sps,:eq,:sum,1w,:offset,$(name)+$(atlas.offset),:legend
@@@

