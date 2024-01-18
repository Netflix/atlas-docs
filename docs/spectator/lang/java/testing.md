# Testing

Testing should be relatively straightforward if you are using injection for the
[Registry](registry/overview.md). Consider a sample class:

```java
public class Foo {

  private final Counter counter;

  @Inject
  public Foo(Registry registry) {
    counter = registry.counter("foo");
  }

  public void doSomething() {
    counter.increment();
  }
}
```

Tests will typically want to use an isolated instance of the `DefaultRegistry`.

## Simple Test

A basic standalone test class would look something like:

```java
public class FooTest {

  private Registry registry;
  private Foo foo;

  @Before
  public void init() {
    registry = new DefaultRegistry();
    foo = new Foo(registry);
  }

  @Test
  public void doSomething() {
    foo.doSomething();
    Assert.assertEquals(1, registry.counter("foo").count());
  }
}
```

## Spring Test

If using Spring, then you can create a binding for the `DefaultRegistry`, for example:

```java
public class FooTest {

  private Registry registry;
  private Foo foo;

  @Configuration
  public static class TestConfiguration {
    @Bean
    public Registry registry() {
      return new DefaultRegistry();
    }

    @Bean
    public Foo foo(Registry registry) {
      return new Foo(registry);
    }
  }

  private AnnotationConfigApplicationContext createContext() {
    AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext();
    context.register(TestConfiguration.class);
    context.refresh();
    return context;
  }

  @Test
  public void doSomething() {
    try (AnnotationConfigApplicationContext context = createContext()) {
      Foo foo = context.getBean(Foo.class);
      foo.doSomething();

      Registry registry = context.getBean(Registry.class);
      Assert.assertEquals(1, registry.counter("foo").count());
    }
  }
}
```

## Exceptions

By default, for most user errors Spectator will log a warning rather than throw an exception.
The rationale is that users do not often think about instrumentation and logging code causing
an exception and interrupting the control flow of a program. However, for test cases it is
recommended to be more aggressive and learn about problems as early as possible. This can
be done by setting a system property:

```
spectator.api.propagateWarnings=true
```

Consider an example:

```java
private static final Id RARE_EXCEPTION_ID = null;

public void doSomethingImportant() {
  try {
    ... do work ...
  } catch (RareException e) {
    // There is a bug in the program, an Id is not allowed to be null. In production we do
    // not want it to throw and interrupt the control flow. Instrumentation should gracefully
    // degrade.
    registry.counter(RARE_EXCEPTION_ID).increment();

    // These statements are important to provide context for operating the system
    // and to ensure the app continues to function properly.
    LOGGER.error("important context for user", e);
    properlyHandleException(e);
  }
}
```
