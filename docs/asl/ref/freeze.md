@@@ atlas-signature
...
-->
<empty>
@@@

Remove all items from the main stack and move them to a separate frozen stack that
cannot be modified except by additional `:freeze` operations. At the end of execution,
the final result includes both the frozen contents and any items remaining on the main stack.

This operation is essential for protecting certain expressions from being modified by
stack manipulation operations, particularly useful when building dashboard templates
for overlay expressions.

## Parameters

* **...**: All items currently on the main stack (variable number of arguments)

## Key Behavior

1. **Isolation**: Frozen items are protected from further stack manipulation
2. **Preservation**: Frozen items maintain their original order
3. **Accumulation**: Multiple `:freeze` operations add to the frozen stack
4. **Final output**: Frozen items appear in the final result alongside main stack items

## Primary Use Case: Overlays on Dashboards

The most common use case is protecting overlay expressions for graphs on a dashboard.
Consider an overlay showing network errors that should appear on all graphs in a dashboard,
regardless of filtering:

**Problem**: Dashboard filtering affects all expressions:
```
# This filtering would break the overlay
,:list,(,nf.cluster,{{selected_cluster}},:eq,:cq,),:each
```

**Solution**: Freeze the overlay to protect it:
```
# Protected overlay expression - won't be affected by filtering
name,networkErrors,:eq,:sum,50,:gt,:vspan,40,:alpha,
:freeze,

# Main dashboard content - will be filtered
name,ssCpuUser,:eq,:avg,1,:axis,
name,loadavg1,:eq,:avg,2,:axis,

# Dashboard filtering - only applies to main stack
:list,(,nf.cluster,{{selected_cluster}},:eq,:cq,),:each
```

*Since: 1.6*

## Examples

Basic freeze operation:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,:freeze
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>c</td>
<td>c</td>
</tr><tr>
<td>1</td>
<td>b</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>

This moves `a`, `b`, and `c` from the main stack to the frozen stack, where they
cannot be modified by subsequent operations.

## Related Operations

* [:cq](cq.md) - Common query operation that freeze is often used to protect against
* [:list](list.md) - List operation that freeze prevents from affecting protected expressions
* [:each](each.md) - Iteration operation that operates only on the main stack