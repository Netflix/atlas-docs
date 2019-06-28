
Node.js runtime heap space metrics, provided by [spectator-js-nodejsmetrics](../usage.md#spectator-js-nodejsmetrics).

## Metrics

Data is gathered from the [v8.getHeapSpaceStatistics] method, for each space listed.

Space categories:

* `new_space`: Where new allocations happen; it is fast to allocate and collect garbage here.
Objects living in the New Space are called the Young Generation. 
* `old_space`: Object that survived the New Space collector are promoted here; they are called
the Old Generation. Allocation in the Old Space is fast, but collection is expensive so it is
less frequently performed.
* `code_space`: Contains executable code and therefore is marked executable.
* `map_space`: Contains map objects only.
* `large_object_space`: Contains promoted large objects which exceed the size limits of other
spaces. Each object gets its own `mmap` region of memory and these objects are never moved by GC.

[v8.getHeapSpaceStatistics]: https://nodejs.org/api/v8.html#v8_v8_getheapspacestatistics

### Common Dimensions

The following dimensions are common to the metrics published by this module:

* `nodejs.version`: The version of the Node.js runtime.

### nodejs.spaceSize

The allocated size of the space.

**Unit:** bytes

**Dimensions:**

* `id`: Space category.

### nodejs.spaceUsedSize

The used size of the space.

**Unit:** bytes

**Dimensions:**

* `id`: Space category.

### nodejs.spaceAvailableSize

The available size of the space.

**Unit:** bytes

**Dimensions:**

* `id`: Space category.

### nodejs.physicalSpaceSize

The physical size of the space.

**Unit:** bytes

**Dimensions:**

* `id`: Space category.
