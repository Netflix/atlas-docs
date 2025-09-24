@@@ atlas-signature
top: Any
second: Any
-->
second: Any
top: Any
second: Any
@@@

Copy the item in the second position on the stack to the top, leaving the original item in place.
This allows you to access an item that's buried under the top item without losing the top item.

## Parameters

* **top**: The item currently at the top of the stack (remains in place)
* **second**: The item in the second position that will be copied to the top

## Examples

Basic over operation:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:over
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td></td>
<td>a</td>
</tr></tbody></table>

Common pattern - apply the same operation to two different expressions:

@@@ atlas-stacklang
/api/v1/graph?q=name,cpu,:eq,:sum,name,memory,:eq,:sum,:over,:add
@@@

## Related Operations

* [:dup](dup.md) - Duplicate the top item
* [:swap](swap.md) - Exchange the top two items
* [:tuck](tuck.md) - Copy the top item to the third position
* [:rot](rot.md) - Rotate three items (bottom to top)