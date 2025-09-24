@@@ atlas-signature
...
-->
<empty>
@@@

Remove all items from the stack, leaving it completely empty. This is useful for resetting
the stack state during complex expression building or when you need to discard all accumulated
intermediate results.

## Parameters

* **...**: All items currently on the stack (variable number of arguments)

## Behavior

* **Complete removal**: Removes every item from the stack regardless of count or type
* **Empty result**: Stack becomes completely empty after execution
* **Destructive**: All stack contents are permanently lost (cannot be recovered)

## Examples

Clearing a stack with multiple items:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,:clear
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>c</td>
<td></td>
</tr><tr>
<td>1</td>
<td>b</td>
<td></td>
</tr><tr>
<td>2</td>
<td>a</td>
<td></td>
</tr></tbody></table>

## Related Operations

* [:drop](drop.md) - Remove single item from stack
* [:ndrop](ndrop.md) - Remove N items from stack (partial clearing)
* [:depth](depth.md) - Check stack depth before clearing
* [:freeze](freeze.md) - Preserve items before clearing (protects from clearing)