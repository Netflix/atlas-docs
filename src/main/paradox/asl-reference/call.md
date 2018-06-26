
# call

## Signature

`? List -- ?`

## Summary

Pop a list off the stack and execute it as a program. The required inputs and result of the
stack depend on the operations in the list. For example, to square the argument on
the top of the stack:

@@@ atlas-expr
2,(,:dup,:mul,),:call
@@@

To use as part of a user defined function, see the @ref:[fcall](fcall.md) operation.