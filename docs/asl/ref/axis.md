@@@ atlas-signature
Query
-->
StyleExpr
@@@

Change the line style to stack instead of the default of individual lines. 
In this mode the line will be filled to the previous stacked line on the same axis.

Example:

@@@ atlas-example { hilite=:stack }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:stack
@@@
