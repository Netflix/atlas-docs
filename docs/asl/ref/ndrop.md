@@@ atlas-signature
n: Int
...
-->
...
@@@

Remove the top N items from the stack. Unlike [:drop](drop.md) which removes only one item,
this operator can remove multiple items at once. This is useful for stack cleanup operations
and discarding intermediate results during complex expression building.

## Parameters

* **...**: The stack items to potentially remove (at least N items should be present)
* **n**: Number of items to remove from the top of the stack (non-negative integer)

## Behavior

1. **Item removal**: Removes the top N items from the stack (N = 0 removes nothing)
2. **Stack preservation**: Items below the top N remain unchanged on the stack
3. **Boundary handling**: If N exceeds available items, removes all available items
4. **Error handling**: Throws exception if N parameter is missing

## Examples

Removing no items (N = 0):

@@@ atlas-stacklang
/api/v1/graph?q=a,0,:ndrop
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

Removing 2 items from the stack:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,2,:ndrop
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>2</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>c</td>
<td></td>
</tr><tr>
<td>2</td>
<td>b</td>
<td></td>
</tr><tr>
<td>3</td>
<td>a</td>
<td></td>
</tr></tbody></table>

Requesting to remove more items than available (removes all 3 available):

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,4,:ndrop
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>4</td>
<td></td>
</tr><tr>
<td>1</td>
<td>c</td>
<td></td>
</tr><tr>
<td>2</td>
<td>b</td>
<td></td>
</tr><tr>
<td>3</td>
<td>a</td>
<td></td>
</tr></tbody></table>

Error case (missing N parameter):

@@@ atlas-stacklang
/api/v1/graph?q=,:ndrop
@@@

!!! warning
    Throws an exception due to missing the `N` parameter.

## Related Operations

* [:drop](drop.md) - Remove single item from stack (N = 1 equivalent)
* [:nlist](nlist.md) - Create list from N items (complementary operation)
* [:list](list.md) - Remove all items to create list
* [:swap](swap.md) / [:over](over.md) - Reorder items instead of removing them