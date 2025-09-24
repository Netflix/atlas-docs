@@@ atlas-signature
top: Any
second: Any
-->
top: Any
second: Any
top: Any
second: Any
@@@

Copy both items from the stack and place copies on top. This operator provides a convenient
way to duplicate both items on a two-item stack. It's equivalent to the sequence `:over,:over`
but more clearly expresses the intent to copy both items.

## Parameters

* **top**: The item on top of the stack (will be copied)
* **second**: The second item from the top (will be copied)

## Examples

Copying two items from deeper stack positions:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:2over
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
</tr><tr>
<td>3</td>
<td></td>
<td>a</td>
</tr></tbody></table>

## Equivalent Sequence

The `:2over` operation is exactly equivalent to:

```
:over,:over
```

Both sequences produce the same result, but `:2over` is more concise and clearly indicates
the intent to copy two items from deeper positions.

## Related Operations

* [:over](over.md) - Copy single item from second position (component operation)
* [:pick](pick.md) - Copy item from arbitrary position (more general)
* [:dup](dup.md) - Copy top item only
* [:nip](nip.md) - Remove second item (opposite of adding)
* [:tuck](tuck.md) - Copy top item to third position