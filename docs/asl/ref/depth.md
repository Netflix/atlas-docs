@@@ atlas-signature
...
-->
count: Int
...
@@@

Push the current stack depth (number of items) onto the stack. This introspection operator
allows you to inspect the stack state and make decisions based on how many items are present.
The original stack contents remain unchanged.

## Parameters

* **...**: The current stack contents (any number of items)

## Behavior

* **Non-destructive**: Original stack items remain in their positions
* **Count calculation**: Counts all items currently on the stack
* **Stack growth**: Adds one more item (the count) to the stack
* **Zero handling**: Empty stack returns depth of 0

## Examples

Empty stack depth:

@@@ atlas-stacklang
/api/v1/graph?q=,:depth
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td></td>
<td>0</td>
</tr></tbody></table>

Single item stack depth:

@@@ atlas-stacklang
/api/v1/graph?q=a,:depth
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>a</td>
<td>1</td>
</tr><tr>
<td>1</td>
<td></td>
<td>a</td>
</tr></tbody></table>

Multiple items stack depth:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:depth
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td>2</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td></td>
<td>a</td>
</tr></tbody></table>

## Related Operations

* [:clear](clear.md) - Remove all items (sets depth to 0)
* [:drop](drop.md) - Remove single item (decreases depth by 1)
* [:ndrop](ndrop.md) - Remove N items (decreases depth by N)
* [:dup](dup.md) - Duplicate item (increases depth by 1)
* [:nlist](nlist.md) - Create list from N items (requires depth >= N)

Since: 1.5.0