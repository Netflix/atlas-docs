# SpectatorD Metrics

### spectator.measurements

The number of measurements that have either been sent to an Atlas backend or dropped.

**Unit:** measurements/second

**Dimensions:**

* `id`: One of `sent` or `dropped`.
* `error`: The type of error that occurred, one of `http-error`, `validation`, or `other`.
* `owner`: `spectatord`
* Common Infrastructure

### spectator.registrySize

The number of measurements stored in the registry.

**Unit:** measurements

**Dimensions:**

* `owner`: `spectatord`
* Common Infrastructure

### spectatord.parsedCount

The number of input lines parsed.

**Unit:** lines/second

**Dimensions:**

* Common Infrastructure

### spectatord.parseErrors

The number of errors that have occurred while parsing input lines.

**Unit:** lines/second

**Dimensions:**

* Common Infrastructure

### spectatord.percentileCacheSize

The number of Distribution Summaries and/or Percentile Timers that have been updated recently in
the dedicated cache.

**Unit:** meters

**Dimensions:**

* `id`: One of `dist-summary` or `timer`.
* Common Infrastructure

### spectatord.percentileExpired

The number of Distribution Summaries and/or Percentile Timers that have been expired from the
dedicated cache.

**Unit:** meters/second

**Dimensions:**

* `id`: One of `dist-summary` or `timer`.
* Common Infrastructure

### spectatord.poolAllocSize

The size of the internal string pool.

**Unit:** bytes

**Dimensions:**

* Common Infrastructure

### spectatord.poolEntries

The number of entries in the internal string pool.

**Unit:** entries
