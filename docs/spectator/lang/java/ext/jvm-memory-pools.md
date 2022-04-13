# Memory Pools

Uses the [MemoryPoolMXBean](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/MemoryPoolMXBean.html)
provided by the JDK to monitor the sizes of java memory spaces such as perm gen, eden, old gen, etc. 

## Getting Started

To get information about memory pools in Spectator, just setup registration of standard MXBeans.
Note, if you are building an app at Netflix, then this should happen automatically via the normal
platform initialization.

```java
import com.netflix.spectator.jvm.Jmx;

Jmx.registerStandardMXBeans(registry);
```

## Metrics

### jvm.memory.used

Gauge reporting the current amount of memory used. For the young and old gen pools this
metric will typically have a sawtooth pattern. For alerting or detecting memory pressure
the [live data size](jvm-gc.md#jvmgclivedatasize)
is probably a better option.

**Unit:** bytes

**Dimensions:**

* See [metric dimensions](#metric-dimensions).

### jvm.memory.committed

Gauge reporting the current amount of memory committed. From the
[javadocs](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/MemoryUsage.html),
committed is:

> The amount of memory (in bytes) that is guaranteed to be available for use by the Java
> virtual machine. The amount of committed memory may change over time (increase or decrease).
> The Java virtual machine may release memory to the system and committed could be less than
> init. committed will always be greater than or equal to used.

**Unit:** bytes 

**Dimensions:**

* See [metric dimensions](#metric-dimensions).

### jvm.memory.max

Gauge reporting the max amount of memory that can be used. From the
[javadocs](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/MemoryUsage.html),
max is:

> The maximum amount of memory (in bytes) that can be used for memory management. Its value
> may be undefined. The maximum amount of memory may change over time if defined. The amount
> of used and committed memory will always be less than or equal to max if max is defined. A
> memory allocation may fail if it attempts to increase the used memory such that
> `used > committed` even if `used <= max` would still be true (for example, when the
> system is low on virtual memory).

**Unit:** bytes 

**Dimensions:**

* See [metric dimensions](#metric-dimensions).

## Metric Dimensions

All memory metrics have the following dimensions:

* `id`: name of the memory pool being reported. The names of the pools vary depending on the
  garbage collector algorithm being used.
* `memtype`: type of memory. It has two possible values: `HEAP` and `NON_HEAP`. For more
  information see the javadocs for [MemoryType](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/MemoryType.html).
