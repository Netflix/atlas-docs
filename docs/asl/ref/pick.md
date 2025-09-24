@@@ atlas-signature
n: Int
...
-->
item: Any
...
@@@

Copy an item from a specific position in the stack and place the copy on top. The original
item remains in its position while a duplicate is added to the top of the stack. This allows
non-destructive access to stack items at arbitrary depths.

## Parameters

* **...**: The current stack contents with at least (n+1) items
* **n**: Zero-based index of the item to copy (0 = top item, 1 = second item, etc.)

## Behavior

* **Non-destructive copying**: Original stack items remain in their positions
* **Index-based access**: Uses zero-based indexing (0 = top, 1 = second from top, etc.)
* **Stack growth**: Adds one more item (the copied item) to the stack
* **Bounds checking**: Index must be valid for current stack depth

## Examples

Picking the top item (index 0) - equivalent to `:dup`:

@@@ atlas-stacklang
/api/v1/graph?q=a,0,:pick
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>0</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>

Picking the top item from a two-item stack:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,0,:pick
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>0</td>
<td>b</td>
</tr><tr>
<td>1</td>
<td>b</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>

Picking the second item (index 1) - equivalent to `:over`:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,1,:pick
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>1</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>b</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>

## Equivalences

* `0,:pick` ≡ `:dup` (copy top item)
* `1,:pick` ≡ `:over` (copy second item)

## Related Operations

* [:dup](dup.md) - Copy top item (equivalent to `0,:pick`)
* [:over](over.md) - Copy second item (equivalent to `1,:pick`)
* [:roll](roll.md) - Move (not copy) item to top of stack
* [:depth](depth.md) - Check stack size before picking
* [:swap](swap.md) - Exchange top two items

Since: 1.5.0