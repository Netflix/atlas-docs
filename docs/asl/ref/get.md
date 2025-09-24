@@@ atlas-signature
key: String
-->
value: Any
@@@

Retrieve the value of a variable from the variable store and push it onto the stack. Variables
are set using the [:set](set.md) operation and can store any type of value including strings,
numbers, expressions, and lists.

This is useful for storing intermediate results, reusing complex expressions, or parameterizing
queries with values that can be changed without modifying the entire expression.

## Parameters

* **key**: The name of the variable whose value should be retrieved

## Examples

Basic variable storage and retrieval:

@@@ atlas-stacklang
/api/v1/graph?q=k,v,:set,k,:get
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>k</td>
<td>v</td>
</tr></tbody></table>

Store and reuse a complex query expression:

@@@ atlas-stacklang
/api/v1/graph?q=baseQuery,name,sps,:eq,nf.app,myapp,:eq,:and,:set,baseQuery,:get,:sum
@@@

## Related Operations

* [:set](set.md) - Store a value in a variable
* [:sset](sset.md) - Store a value and also leave it on the stack