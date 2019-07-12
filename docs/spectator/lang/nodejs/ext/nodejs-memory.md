
Node.js runtime memory metrics, provided by [spectator-js-nodejsmetrics](../usage.md#spectator-js-nodejsmetrics).

## Metrics

### Common Dimensions

The following dimensions are common to the metrics published by this module:

* `nodejs.version`: The version of the Node.js runtime.

### nodejs.rss

Resident Set Size, which is the total memory allocated for the process execution. This includes
the Code Segment, Stack (local variables and pointers) and Heap (objects and closures).

**Unit:** bytes

### nodejs.heapTotal

Total size of the allocated heap.

**Unit:** bytes

### nodejs.heapUsed

Memory used during the execution of our process.

**Unit:** bytes

### nodejs.external

Memory usage of C++ objects bound to JavaScript objects managed by V8.

**Unit:** bytes
