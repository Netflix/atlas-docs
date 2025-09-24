@@@ atlas-signature
function: List
items: List
-->
List(function(items[0]), ..., function(items[N-1]))
@@@

Create a new list by applying a function to each element of the input list. The function is applied
to each element individually, and the results are collected into a new list. This is a functional
programming concept similar to map operations in other languages.

## Parameters

* **items**: The input list containing elements to be transformed
* **function**: A list representing the function to apply to each element

## Examples

Apply a format function to transform each string in a list:

@@@ atlas-stacklang
/api/v1/graph?q=(,a%s,b%s,),(,(,.netflix.com,),:format,),:map
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>List((, .netflix.com, ), :format)</td>
<td>List(a.netflix.com, b.netflix.com)</td>
</tr><tr>
<td>1</td>
<td>List(a%s, b%s)</td>
<td></td>
</tr></tbody></table>

This example takes the list `(a%s, b%s)` and applies the function `(, .netflix.com, ), :format` to each
element, resulting in `a.netflix.com` and `b.netflix.com`.

## Related Operations

* [:each](each.md) - Execute a function for each element but don't collect results
* [:format](format.md) - String formatting function commonly used with map
* [:list](list.md) - Create lists that can be transformed with map