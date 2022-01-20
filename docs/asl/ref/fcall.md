@@@ atlas-signature
String
...
-->
?
@@@

Shorthand equivalent to writing: `:get,:call` 

Example:

@@@ atlas-stacklang
/api/v1/graph?q=duplicate,(,:dup,),:set,a,duplicate,:fcall
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>duplicate</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>