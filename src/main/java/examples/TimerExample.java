package examples;

import com.netflix.spectator.api.Registry;
import com.netflix.spectator.api.Timer;

import javax.inject.Inject;
import java.util.concurrent.TimeUnit;


// #setup
public class TimerExample {

  private final Registry registry;
  private final Timer requestLatency;

  @Inject
  public TimerExample(Registry registry) {
    this.registry = registry;
    requestLatency = registry.timer("server.requestLatency");
  }
  // #setup

  // #using-lambda
  public Response handleUsingLambda(Request request) throws Exception {
    return requestLatency.record(() -> handleImpl(request));
  }
  // #using-lambda

  // #explicitly
  public Response handleExplicitly(Request request) {
    final long start = registry.clock().monotonicTime();
    try {
      return handleImpl(request);
    } finally {
      final long end = registry.clock().monotonicTime();
      requestLatency.record(end - start, TimeUnit.NANOSECONDS);
    }
  }
  // #explicitly

  private Response handleImpl(Request request) {
    // do something useful
    return new Response();
  }

  public static class Request {
  }

  public static class Response {
  }
}
