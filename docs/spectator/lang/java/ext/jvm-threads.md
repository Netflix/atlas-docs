# Threads

Uses the [ThreadMXBean](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/ThreadMXBean.html)
provided by the JDK to monitor the number of active threads and threads started.

## Getting Started

To get information about threads in Spectator, just setup registration of standard MXBeans. Note,
if you are building an app at Netflix, then this should happen automatically via the normal platform
initialization.

```java
import com.netflix.spectator.jvm.Jmx;

Jmx.registerStandardMXBeans(registry);
```

## Metrics

### jvm.thread.threadCount

Gauge reporting the number of active threads.

**Unit:** threads

**Dimensions:**

* `id`: thread category, either `daemon` or `non-daemon`

### jvm.thread.threadsStarted

Counter reporting the number of threads started.

**Unit:** threads/second

**Dimensions:**

* None.
