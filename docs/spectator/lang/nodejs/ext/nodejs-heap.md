
Node.js runtime heap metrics, provided by [spectator-js-nodejsmetrics](../usage.md#spectator-js-nodejsmetrics).

## Metrics

Data is gathered from the [v8.getHeapStatistics] method.

[v8.getHeapStatistics]: https://nodejs.org/api/v8.html#v8_v8_getheapstatistics

### Common Dimensions

The following dimensions are common to the metrics published by this module:

* `nodejs.version`: The version of the Node.js runtime.

### nodejs.doesZapGarbage

Whether or not the `--zap_code_space` option is enabled.

This makes V8 overwrite heap garbage with a bit pattern. The RSS footprint (resident memory set)
gets bigger because it continuously touches all heap pages and that makes them less likely to get
swapped out by the operating system.

**Unit:** boolean

### nodejs.heapSizeLimit

The absolute limit the heap cannot exceed (default limit or `--max_old_space_size`).

**Unit:** bytes

### nodejs.mallocedMemory

Current amount of memory, obtained via `malloc`.

**Unit:** bytes

### nodejs.peakMallocedMemory

Peak amount of memory, obtained via `malloc`.

**Unit:** bytes

### nodejs.totalAvailableSize

Available heap size.

**Unit:** bytes

### nodejs.totalHeapSize

Memory V8 has allocated for the heap. This can grow if `usedHeap` needs more.

**Unit:** bytes

### nodejs.totalHeapSizeExecutable

Memory for compiled bytecode and JITed code.

**Unit:** bytes

### nodejs.totalPhysicalSize

Committed size.

**Unit:** bytes

### nodejs.usedHeapSize

Memory used by application data.

**Unit:** bytes
