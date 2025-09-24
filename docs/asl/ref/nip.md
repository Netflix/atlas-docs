@@@ atlas-signature
top: Any
second: Any
-->
top: Any
@@@

Remove the second item from the stack while keeping the top item. This operator provides a
convenient way to discard the item below the top without affecting the top item. It's equivalent
to the sequence `:swap,:drop` but expresses the intent more clearly.

## Parameters

* **second**: The item in the second position (will remain)
* **top**: The item on top of the stack (will be removed)

## Behavior

* **Selective removal**: Removes only the second item, preserving the top
* **Stack shrinkage**: Reduces stack size by one
* **Order preservation**: Top item remains on top after operation

## Examples

Removing the second item while keeping the top:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:nip
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td>b</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td></td>
</tr></tbody></table>

## Equivalent Sequence

The `:nip` operation is exactly equivalent to:

```
:swap,:drop
```

Both sequences produce the same result, but `:nip` is more concise and expressive.

## Related Operations

* [:drop](drop.md) - Remove top item (different position)
* [:swap](swap.md) - Exchange positions (component of nip)
* [:over](over.md) - Copy second item to top (opposite of removing)
* [:tuck](tuck.md) - Copy top item below second (different stack growth)
* [:2over](2over.md) - Copy two items from deeper positions
