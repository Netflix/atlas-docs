@@@ atlas-signature
key: String
...
-->
Any
@@@

Function call by variable name. This is equivalent to `:get,:call` - it retrieves a stored
program from the variable store and executes it. This provides a convenient shorthand for
calling stored functions without separate get and call operations.

## Parameters

* **key**: The variable name containing the program to execute
* **...**: Additional stack items that may be consumed by the called program

## Behavior

The operation performs these steps:
1. Retrieves the value stored under `key` from the variable store
2. Executes the retrieved value as a program using `:call` semantics
3. The program can consume additional stack items and produce any output

## Examples

Storing and calling a function:

@@@ atlas-stacklang
/api/v1/graph?q=duplicate,(,:dup,),:set,a,duplicate,:fcall
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>duplicate</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>

This example:
1. Sets a program `(,:dup,)` in variable `duplicate`
2. Puts `a` on the stack
3. Calls the `duplicate` function using `:fcall`
4. The function duplicates `a`, resulting in `a, a` on the stack

Executing a stored function to square the top stack item:

@@@ atlas-example { hilite=:fcall }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=square,(,:dup,:mul,),:set,name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=square,(,:dup,:mul,),:set,name,sps,:eq,:sum,square,:fcall
@@@

This stores the squaring program `(,:dup,:mul,)` in variable `square`, then calls it using
`:fcall`. The program duplicates the sum result and multiplies the copies together,
effectively squaring the value.

## Related Operations

* [:call](call.md) - Execute a program directly from the stack
* [:get](get.md) - Retrieve values from variable store (used internally by fcall)
* [:set](set.md) - Store programs in variables for later calling
* [:list](list.md) - Create program lists for storage and execution