# Buffer Pools

Buffer pools, such as direct byte buffers, can be monitored at a high level using the
[BufferPoolMXBean](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/BufferPoolMXBean.html)
provided by the JDK.

## Getting Started

To get information about buffer pools in Spectator, just setup registration of standard MXBeans.
Note, if you are building an app at Netflix, then this should happen automatically via the normal
platform initialization.

```java
import com.netflix.spectator.jvm.Jmx;

Jmx.registerStandardMXBeans(registry);
```

## Metrics

### jvm.buffer.count

Gauge showing the current number of distinct buffers.

**Unit:** count

**Dimensions:**

* `id`: type of buffers. Value will be either `direct` for direct byte buffers or `mapped` for
  memory mapped files.

### jvm.buffer.memoryUsed

Gauge showing the current number of bytes used by all buffers.

**Unit:** bytes

**Dimensions:**

* `id`: type of buffers. Value will be either `direct` for direct byte buffers or `mapped` for
  memory mapped files.
