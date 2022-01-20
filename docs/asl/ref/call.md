@@@ atlas-signature
?
List
-->
?
@@@

Pops a list off the stack and executes it as a program.

Example:

@@@ atlas-stacklang
/api/v1/graph?q=(,a,),:call
@@@

| Pos | Input   | Output|
|-----|---------|-------|
| 0   | List(a) | a     |
