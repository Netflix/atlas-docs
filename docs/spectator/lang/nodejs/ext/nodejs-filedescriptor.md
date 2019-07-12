
Node.js runtime file descriptor metrics, provided by [spectator-js-nodejsmetrics](../usage.md#spectator-js-nodejsmetrics).

## Metrics

### Common Dimensions

The following dimensions are common to the metrics published by this module:

* `nodejs.version`: The version of the Node.js runtime.

### openFileDescriptorsCount

Number of file descriptors currently open.

**Unit:** file descriptors

### maxFileDescriptorsCount

The maximum number of file descriptors that can be open at the same time.

**Unit:** file descriptors
