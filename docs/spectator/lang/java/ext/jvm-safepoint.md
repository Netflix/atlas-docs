# Safepoint

Uses Hotspot mbean to access the spent in and getting to [safepoints].

[safepoints]: https://shipilev.net/jvm/anatomy-quarks/22-safepoint-polls/

## Getting Started

To get information about compilation in Spectator, just setup registration of standard MXBeans.
Note, if you are building an app at Netflix, then this should happen automatically via the normal
platform initialization.

```java
import com.netflix.spectator.jvm.Jmx;

Jmx.registerStandardMXBeans(registry);
```

## Metrics

### jvm.hotspot.safepointTime

Timer reporting the amount of time the application has been stopped for safepoint operations.

**Unit:** seconds

### jvm.hotspot.safepointSyncTime

Timer reporting the amount of time spent getting to safepoints.

**Unit:** seconds