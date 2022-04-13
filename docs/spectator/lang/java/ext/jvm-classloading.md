# Class Loading

Uses the [ClassLoadingMXBean](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/ClassLoadingMXBean.html)
provided by the JDK to monitor the number of classes loaded and unloaded.

## Getting Started

To get information about classloading in Spectator, just setup registration of standard MXBeans.
Note, if you are building an app at Netflix, then this should happen automatically via the normal
platform initialization.

```java
import com.netflix.spectator.jvm.Jmx;

Jmx.registerStandardMXBeans(registry);
```

## Metrics

### jvm.classloading.classesLoaded

Counter reporting the number of classes loaded.

**Unit:** classes/second

**Dimensions:**

* None.

### jvm.classloading.classesUnloaded

Counter reporting the number of classes unloaded.

**Unit:** classes/second

**Dimensions:**

* None.
