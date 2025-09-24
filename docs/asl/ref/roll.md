@@@ atlas-signature
n: Int
...
-->
item: Any
...
@@@

Move an item from a specific position in the stack to the top. Unlike [:pick](pick.md) which
copies an item, `:roll` removes the item from its original position and places it on top.
This is useful for reorganizing the stack when you need to bring buried items to the surface.

## Parameters

* **...**: The current stack contents with at least (n+1) items
* **n**: Zero-based index of the item to move (0 = top item, 1 = second item, etc.)

## Examples

Rolling the top item (index 0) - effectively a no-op:

@@@ atlas-stacklang
/api/v1/graph?q=a,0,:roll
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>0</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td></td>
</tr></tbody></table>

Rolling the top item from a two-item stack:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,0,:roll
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>0</td>
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

Rolling the second item (index 1) to the top:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,1,:roll
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
<td></td>
</tr></tbody></table>

## Difference from Pick

| Operation | Effect | Stack Size Change |
|-----------|--------|-------------------|
| `:pick` | **Copy** item to top | +1 (grows) |
| `:roll` | **Move** item to top | 0 (unchanged) |

## Related Operations

* [:pick](pick.md) - Copy (not move) item to top of stack
* [:rot](rot.md) / [:-rot](-rot.md) - Rotate top three items
* [:swap](swap.md) - Exchange top two items (equivalent to `1,:roll`)
* [:depth](depth.md) - Check stack size before rolling
* [:over](over.md) - Copy second item (non-destructive alternative)

Since: 1.5.0