@@@ atlas-signature
List
-->
?
@@@

Pops a list off the stack and executes it as a program. 

Example:

@@@ atlas-stacklang
/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=(,a,),:call
@@@

| Pos | Input | Output|
|-----|-------|-------|
| 0   | List(a) | a  |
