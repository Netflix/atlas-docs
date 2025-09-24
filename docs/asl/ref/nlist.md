@@@ atlas-signature
n: Int
...
-->
List[?]
...
@@@

Create a list from the top N items on the stack. Unlike [:list](list.md) which consumes the
entire stack, this operator only takes a specified number of items and leaves the rest of
the stack intact. This is useful for selective list creation without affecting other stack items.

## Parameters

* **...**: The stack items to potentially include in the list (at least N items must be present)
* **n**: Number of items to take from the top of the stack (non-negative integer)

## Behavior

1. **Item selection**: Takes the top N items from the stack (N = 0 creates an empty list)
2. **List creation**: Creates a list preserving stack order (top item becomes last list element)
3. **Stack preservation**: Items below the top N remain unchanged on the stack
4. **Boundary handling**: If N exceeds available items, takes all available items

## Examples

Creating an empty list (N = 0):

@@@ atlas-stacklang
/api/v1/graph?q=a,0,:nlist
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>0</td>
<td>List()</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>

Taking 2 items from the stack:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,2,:nlist
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>2</td>
<td>List(b, c)</td>
</tr><tr>
<td>1</td>
<td>c</td>
<td>a</td>
</tr><tr>
<td>2</td>
<td>b</td>
<td></td>
</tr><tr>
<td>3</td>
<td>a</td>
<td></td>
</tr></tbody></table>

Requesting more items than available (takes all 3 available):

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,4,:nlist
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>4</td>
<td>List(a, b, c)</td>
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

## Related Operations

* [:list](list.md) - Create list from entire stack (consumes all items)
* [:ndrop](ndrop.md) - Remove N items from stack (opposite operation)
* [:each](each.md) - Process lists created with :nlist
* [:map](map.md) - Transform lists created with :nlist

Since: 1.5.0