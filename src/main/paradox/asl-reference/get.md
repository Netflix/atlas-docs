
# get

## Signature

`k -- v`

## Summary

Pop the key and push the value associated with that key on top of the stack. The key
must have been previously associated with a value using the @ref:[set](set.md) operation.

## Example

@@@ atlas-expr
-- Set the value for PI,
pi,3.14159,:set,

-- Get the value for PI,
pi,:get
@@@

