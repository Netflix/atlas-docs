
Node.js runtime event loop metrics, provided by [spectator-js-nodejsmetrics](../usage.md#spectator-js-nodejsmetrics).

## Metrics

### Common Dimensions

The following dimensions are common to the metrics published by this module:

* `nodejs.version`: The version of the Node.js runtime.

### nodejs.eventLoop

The time it takes for the event loop to complete. This is sampled twice per second.

**Unit:** seconds

### nodejs.eventLoopLag

The time that the event loop is running behind, as measured by attempting to execute
a timer once per second.

**Unit:** seconds
