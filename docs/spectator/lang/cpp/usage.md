# spectator-cpp Usage

C++ thin-client [metrics library] for use with [Atlas] and [SpectatorD].

[metrics library]: https://github.com/Netflix/spectator-cpp
[Atlas]: ../../../overview.md
[SpectatorD]: ../../agent/usage.md

## Instrumenting Code

```C++
#include <spectator/registry.h>

// use default values
static constexpr auto kDefault = 0;

struct Request {
  std::string country;
};

struct Response {
  int status;
  int size;
};

class Server {
 public:
  explicit Server(spectator::Registry* registry)
      : registry_{registry},
        request_count_id_{registry->CreateId("server.requestCount", spectator::Tags{})},
        request_latency_{registry->GetTimer("server.requestLatency")},
        response_size_{registry->GetDistributionSummary("server.responseSizes")} {}

  Response Handle(const Request& request) {
    auto start = std::chrono::steady_clock::now();

    // do some work and obtain a response...
    Response res{200, 64};

    // Update the Counter id with dimensions, based on information in the request. The Counter
    // will be looked up in the Registry, which is a fairly cheap operation, about the same as
    // the lookup of an id object in a map. However, it is more expensive than having a local
    // variable set to the Counter.
    auto cnt_id = request_count_id_
        ->WithTag("country", request.country)
        ->WithTag("status", std::to_string(res.status));
    registry_->GetCounter(std::move(cnt_id))->Increment();
    request_latency_->Record(std::chrono::steady_clock::now() - start);
    response_size_->Record(res.size);
    return res;
  }

 private:
  spectator::Registry* registry_;
  std::shared_ptr<spectator::Id> request_count_id_;
  std::shared_ptr<spectator::Timer> request_latency_;
  std::shared_ptr<spectator::DistributionSummary> response_size_;
};

Request get_next_request() {
  return Request{"US"};
}

int main() {
  auto logger = spdlog::stdout_color_mt("console"); 
  std::unordered_map<std::string, std::string> common_tags{{"xatlas.process", "some-sidecar"}};
  spectator::Config cfg{"unix:/run/spectatord/spectatord.unix", common_tags};
  spectator::Registry registry{std::move(cfg), logger);

  Server server{&registry};

  for (auto i = 1; i <= 3; ++i) {
    // get a request
    auto req = get_next_request();
    server.Handle(req);
  }
}
```

## Usage

We do not publish this library as a binary artifact, because it can be used across a variety of CPU
and OS platforms, and we do not want to incur this support overheard for a library that is not on
the Paved Path. However, this is a Conan 2 and CMake project, so you can pull the latest code, and
add some build configuration to use it in your project.

As an example of how this is done, see the [atlas-system-agent] project.

* Download the latest `spectator-cpp` code ([conanfile.py#L39-L57]).
* Add the library to your CMake build ([lib/CMakeLists.txt#L1-L32]).

This library has a few dependencies ([conanfile.py#L6-L13]), including a recent `abseil`.

[atlas-system-agent]: https://github.com/Netflix-Skunkworks/atlas-system-agent/tree/main
[conanfile.py#L39-L57]: https://github.com/Netflix-Skunkworks/atlas-system-agent/blob/main/conanfile.py#L39-L57
[lib/CMakeLists.txt#L1-L32]: https://github.com/Netflix-Skunkworks/atlas-system-agent/blob/main/lib/CMakeLists.txt#L1-L32
[conanfile.py#L6-L13]: https://github.com/Netflix/spectator-cpp/blob/main/conanfile.py#L6-L13

### High-Volume Publishing

By default, the library sends every meter change to the `spectatord` sidecar immediately. This
involves a blocking `send` call and underlying system calls, and may not be the most efficient way
to publish metrics in high-volume use cases.

For this purpose, a simple buffering functionality in `Publisher` is implemented, and it can be
turned on by passing a buffer size to the `spectator::Config` constructor ([config.h#L8-L12]). It
is important to note that, until this buffer fills up, the `Publisher` will not send any meters to
the sidecar. Therefore, if your application doesn't emit meters at a high rate, you should either
keep the buffer very small, or do not configure a buffer size at all, which will fall back to the
"publish immediately" mode of operation.

[config.h#L8-L12]: https://github.com/Netflix/spectator-cpp/blob/main/spectator/config.h#L8-L12
