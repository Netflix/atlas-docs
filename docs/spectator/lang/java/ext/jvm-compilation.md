# Compilation

Uses the [CompilationMXBean](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/CompilationMXBean.html)
provided by the JDK to monitor the time spent compiling code, for each compiler name.

## Getting Started

To get information about compilation in Spectator, just setup registration of standard MXBeans.
Note, if you are building an app at Netflix, then this should happen automatically via the normal
platform initialization.

```java
import com.netflix.spectator.jvm.Jmx;

Jmx.registerStandardMXBeans(registry);
```

## Metrics

### jvm.compilation.compilationTime

Counter reporting the amount of elapsed time spent in compilation. If multiple threads are used for
compilation, then this value represents the summation of the time each thread spent in compilation. 

**Unit:** seconds/second

**Dimensions:**

* `compiler`: name of the just-in-time (JIT) compiler
