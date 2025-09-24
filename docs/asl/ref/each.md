@@@ atlas-signature
function: List
items: List
-->
function(items[N-1])
...
function(items[0])
@@@

Execute a function for each element in a list, processing elements in order from first to last.
Unlike [:map](map.md), this operation executes the function for its side effects and places the
results directly on the stack rather than collecting them into a new list.

The function is applied to each element individually, and the results are pushed onto the stack
with the results from the last element ending up on top.

## Parameters

* **items**: The input list containing elements to process
* **function**: A list representing the function/program to execute for each element

## Examples

Apply the `:dup` operation to each element in a list:

@@@ atlas-stacklang
/api/v1/graph?q=(,a,b,),(,:dup,),:each
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>List(:dup)</td>
<td>b</td>
</tr><tr>
<td>1</td>
<td>List(a, b)</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td></td>
<td>a</td>
</tr><tr>
<td>3</td>
<td></td>
<td>a</td>
</tr></tbody></table>

This takes the list `(a, b)` and applies `:dup` to each element:
1. First processes `a`, duplicating it to get `a, a` (pushed to stack)
2. Then processes `b`, duplicating it to get `b, b` (pushed on top)
3. Final stack (top to bottom): `b, b, a, a`

## Related Operations

* [:map](map.md) - Apply function to each element and collect results into a new list
* [:call](call.md) - Execute a single function/program
* [:list](list.md) - Create lists that can be processed with each