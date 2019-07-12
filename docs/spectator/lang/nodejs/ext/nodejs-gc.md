
Node.js runtime garbage collection metrics, provided by [spectator-js-nodejsmetrics](../usage.md#spectator-js-nodejsmetrics).

## Metrics

### Common Dimensions

The following dimensions are common to the metrics published by this module:

* `nodejs.version`: The version of the Node.js runtime.

### nodejs.gc.allocationRate

The rate at which the app is allocating memory.

**Unit:** bytes/second

### nodejs.gc.liveDataSize

The size of the `old_space` after a major GC event.

**Unit:** bytes

### nodejs.gc.maxDataSize

The maximum amount of memory the nodejs process is allowed to use.  This is primarily used
for gaining perspective on the `liveDataSize`.

**Unit:** bytes

### nodejs.gc.pause

The time it takes to complete different GC events.

Event categories:

* `scavenge`: The most common garbage collection method. Node will typically trigger one of
these every time the VM is idle.
* `markSweepCompact`: The heaviest type of garbage collection V8 may do. If you see many of
these happening you will need to either keep fewer objects around in your process or increase
V8's heap limit.
* `incrementalMarking`: A phased garbage collection that interleaves collection with application
logic to reduce the amount of time the application is paused.
* `processWeakCallbacks`: After a garbage collection occurs, V8 will call any weak reference
callbacks registered for objects that have been freed. This measurement is from the start of
the first weak callback to the end of the last for a given garbage collection.

**Unit:** seconds

**Dimensions:**

* `id`: The GC event category.

### nodejs.gc.promotionRate

The rate at which data is being moved from `new_space` to `old_space`.

**Unit:** bytes/second
