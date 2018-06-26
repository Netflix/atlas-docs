
# each

## Signature

`items:List f:List -- f(items[0]) ... f(items[N])`

## Summary

For each item in the input list, push it on the stack and apply a function.

## Example

| **Before**        | **After** |
|-------------------|-----------|
|                   | `9`       |
| `(,:dup,:mul,)`   | `4`       |
| `(,1,2,3,)`       | `1`       |

