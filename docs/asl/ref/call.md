@@@ atlas-signature
program: List
-->
Any
@@@

Pop a list off the stack and execute it as an ASL program. This allows for dynamic
program execution where the program itself can be constructed or stored in variables
and then executed on demand.

## Parameters

* **program**: A list containing ASL expressions to execute

## Examples

Basic program execution:

@@@ atlas-stacklang
/api/v1/graph?q=(,a,),:call
@@@

| Pos | Input   | Output|
|-----|---------|-------|
| 0   | List(a) | a     |

This takes the list `(a)` and executes it as a program, pushing `a` onto the stack.

Executing a program to square the top stack item:

@@@ atlas-example { hilite=:call }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,:dup,:mul,),:call
@@@

This executes the program `(,:dup,:mul,)` which duplicates the top stack item and then
multiplies the two copies together, effectively squaring the value. The program transforms
the sum result by squaring it.

## Related Operations

* [:fcall](fcall.md) - Function call operator
* [:each](each.md) - Execute a function for each element in a list (uses call internally)
* [:map](map.md) - Apply a function to each element in a list
* [:list](list.md) - Create lists that can be executed with call
* [:get](get.md) - Retrieve stored programs from variables
* [:set](set.md) - Store programs in variables for later execution
