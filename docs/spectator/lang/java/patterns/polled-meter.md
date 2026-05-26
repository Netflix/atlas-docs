# Polled Meter

Helper for configuring a meter that will receive a value by regularly polling the source in the
background.

Example usage:

```java
Registry registry = ...
AtomicLong connections = PolledMeter.using(registry)
  .withName("server.currentConnections")
  .monitorValue(new AtomicLong());

// When a connection is added
connections.incrementAndGet();

// When a connection is removed
connections.decrementAndGet();
```

Polling frequency will depend on the underlying Registry implementation, but users should
assume it will be frequently checked and that the provided function is cheap. Users should
keep in mind that polling will not capture all activity, just sample it at some frequency.
For example, if monitoring a queue, then a meter will only tell you the last sampled size
when the value is reported. If more details are needed, then use an alternative type
and ensure that all changes are reported when they occur.

For example, consider tracking the number of currently established connections to a server.
Using a polled meter will show the last sampled number when reported. An alternative would
be to report the number of connections to a Distribution Summary every time a connection is
added or removed. The distribution summary would provide more accurate tracking such as max
and average number of connections across an interval of time. The polled meter would not
provide that level of detail.

If multiple values are monitored with the same id, then the values will be aggregated and
the sum will be reported. For example, registering multiple meters for active threads in
a thread pool with the same id would produce a value that is the overall number of active
threads. For other behaviors, manage it on the user side and avoid multiple registrations.
