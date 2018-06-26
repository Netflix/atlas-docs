
# set

## Signature

`k v -- `

## Summary

Pop the key and value off of the stack and store the value such that it can be retrieved
by using @ref:[get](get.md) with the key.

## Example

@@@ atlas-expr
-- Set the value for PI,
pi,3.14159,:set,

-- Get the value for PI,
pi,:get
@@@

