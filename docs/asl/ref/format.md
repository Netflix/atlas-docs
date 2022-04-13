@@@ atlas-signature
args: List
pattern: String
-->
str: String
@@@

Format a string using a printf [style pattern][formatter].

[formatter]: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Formatter.html

Example:

@@@ atlas-stacklang
/api/v1/graph?q=foo%s,(,bar,),:format
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>List(bar)</td>
<td>foobar</td>
</tr><tr>
<td>1</td>
<td>foo%s</td>
<td></td>
</tr></tbody></table>