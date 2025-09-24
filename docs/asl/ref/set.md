@@@ atlas-signature
value: Any
key: String
-->
@@@

Set the value of a variable in the variable store. Variables can be retrieved later using
[:get](get.md) and are useful for storing intermediate results, reusing complex expressions,
or parameterizing queries.

## Parameters

* **key**: The variable name (string identifier)
* **value**: The value to store (can be any type: string, number, expression, list)

## Examples

Setting a simple variable:

@@@ atlas-stacklang
/api/v1/graph?q=k,v,:set
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>v</td>
<td></td>
</tr><tr>
<td>1</td>
<td>k</td>
<td></td>
</tr></tbody></table>

This stores the value "v" under the key "k", removing both items from the stack.

## Related Operations

* [:get](get.md) - Retrieve stored variable values
* [:sset](sset.md) - Set variables with different stack behavior