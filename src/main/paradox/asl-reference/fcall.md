
# fcall

## Signature

`? name:String -- ?`

## Summary

Invoke a function with the provided name. The function must have previously been stored
with that name using the @ref:[set](set.md) operation. Equivalent to running:

@@@ atlas-expr
,:get,:call
@@@

See the @ref:[call](call.md) operation for more information.

## Example

@@@ atlas-expr
-- Define a function to square the input,
square,(,:dup,:mul,),:set,

-- Use the UDF,
2,square,:fcall
@@@

