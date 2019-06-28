# Java Counters

Counters are created using the [Registry](../registry/overview.md), which is be setup as part of
application initialization. For example:

```java
public class Queue {

  private final Counter insertCounter;
  private final Counter removeCounter;
  private final QueueImpl impl;

  @Inject
  public Queue(Registry registry) {
    insertCounter = registry.counter("queue.insert");
    removeCounter = registry.counter("queue.remove");
    impl = new QueueImpl();
  }
```

Then call increment when an event occurs:

```java
  public void insert(Object obj) {
    insertCounter.increment();
    impl.insert(obj);
  }

  public Object remove() {
    if (impl.nonEmpty()) {
      removeCounter.increment();
      return impl.remove();
    } else {
      return null;
    }
  }
```

Optionally, an amount can be passed in when calling increment. This is useful when a collection of
events happen together. 

```java
  public void insertAll(Collection<Object> objs) {
    insertCounter.increment(objs.size());
    impl.insertAll(objs);
  }
}
```
