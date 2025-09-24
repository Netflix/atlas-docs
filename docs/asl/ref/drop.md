@@@ atlas-signature
item: Any
-->
<empty>
@@@

Remove the item on the top of the stack. This is useful for discarding intermediate
results or cleaning up the stack during complex expression building.

## Parameters

* **item**: The item on top of the stack to remove (can be any type)

## Examples

Removing the top item from a stack with multiple items:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,:drop
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>c</td>
<td>b</td>
</tr><tr>
<td>1</td>
<td>b</td>
<td>a</td>
</tr><tr>
<td>2</td>
<td>a</td>
<td></td>
</tr></tbody></table>

Attempting to drop from an empty stack results in an error:

@@@ atlas-stacklang
/api/v1/graph?q=:drop
@@@

!!! warning
    Throws an exception due to an empty stack.

## Related Operations

* [:dup](dup.md) - Duplicate the top item (opposite of dropping)
* [:swap](swap.md) - Reorder items instead of removing them
* [:over](over.md) - Access items without removing them
* [:list](list.md) - Collect all items into a list instead of dropping them
