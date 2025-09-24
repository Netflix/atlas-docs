@@@ atlas-signature
top: Any
second: Any
-->
second: Any
top: Any
@@@

Exchange the positions of the top two items on the stack. This is one of the most commonly used
stack manipulation operations, often needed when operands are in the wrong order for a binary
operation.

## Parameters

* **top**: The item currently at the top of the stack
* **second**: The item in the second position that will move to the top

## Examples

Basic swap operation:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:swap
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>b</td>
</tr></tbody></table>

Common use case - getting operands in the correct order for division:

@@@ atlas-stacklang
/api/v1/graph?q=name,errors,:eq,:sum,name,requests,:eq,:sum,:swap,:div
@@@

## Related Operations

* [:over](over.md) - Copy the second item to the top
* [:dup](dup.md) - Duplicate the top item
* [:rot](rot.md) - Rotate three items (bottom to top)
* [:-rot](-rot.md) - Rotate three items (top to bottom)