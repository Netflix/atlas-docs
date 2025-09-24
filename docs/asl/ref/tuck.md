@@@ atlas-signature
top: Any
second: Any
-->
top: Any
second: Any
top: Any
@@@

Copy the top item to the third position on the stack. This is equivalent to the sequence `:swap,:over`
and is useful when you need the top item to be accessible after a binary operation.

## Parameters

* **top**: The item currently at the top of the stack that will be copied to the third position
* **second**: The item in the second position (remains unchanged)

## Examples

Basic tuck operation:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:tuck
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td>b</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>a</td>
</tr><tr>
<td>2</td>
<td></td>
<td>b</td>
</tr></tbody></table>

Equivalent sequence using swap and over:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:swap,:over
@@@

## Related Operations

* [:over](over.md) - Copy the second item to the top
* [:swap](swap.md) - Exchange the top two items
* [:dup](dup.md) - Duplicate the top item
