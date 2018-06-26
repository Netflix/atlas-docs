
# map

## Signature

`items:List f:List -- List(f(items[0]) ... f(items[N]))`

## Summary

Create a new list by applying a function to all elements of a list.

## Example

| **Before**       | **After**   |
|------------------|-------------|
| `(,:dup,:mul,)`  |             |
| `(,1,2,3,)`      | `(,1,4,9,)` |

