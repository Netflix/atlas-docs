@@@ atlas-signature
key: String
value: Any
-->
@@@

Set a variable by swapping the stack order first. This is equivalent to `:swap,:set` and
is useful when you have the key and value in the wrong order on the stack.

## Parameters

* **key**: The variable name (string identifier) - expected on second position
* **value**: The value to store (can be any type) - expected on top of stack

## Examples

Setting a variable with swapped stack order:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:sset
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td></td>
</tr><tr>
<td>1</td>
<td>a</td>
<td></td>
</tr></tbody></table>

This is equivalent to: `a,b,:swap,:set` which stores value "a" under key "b".

## Stack Order Difference

* **`:set`** expects: `key, value, :set` (key on bottom, value on top)
* **`:sset`** expects: `value, key, :sset` (value on bottom, key on top)

## Related Operations

* [:set](set.md) - Set variables with standard stack order
* [:swap](swap.md) - Swap stack items (`:sset` includes this operation)
* [:get](get.md) - Retrieve stored variable values
