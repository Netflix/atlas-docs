## Migrating to 2.X

Version 2.X consists of a major rewrite that greatly simplifies spectator-cpp and the process in which it sends metrics to SpectatorD

### New

#### Writers

`spectator.Registry` now supports 3 different writers. The WriterType is specified through a WriterConfig object.

See [Usage > Output Location](usage.md#output-location) for more details.

#### Common Tags

A few local environment common tags are now automatically added to all Meters. Their values are read
from the environment variables.

| Tag          | Environment Variable |
|--------------|----------------------|
| nf.container | TITUS_CONTAINER_NAME |
| nf.process   | NETFLIX_PROCESS_NAME |

Tags from environment variables take precedence over tags passed on code when creating the `Config`.

Note that common tags sourced by [spectatord](https://github.com/Netflix-Skunkworks/spectatord) can't be overwritten.

#### Registry, Config, and Writer Config

* `Config` is now created through a constructor which throws error if the passed in parameters are not valid.
* `WriterConfig` now specifies which writer type the thin client uses.
* `WriterConfig` allows line buffering for all writer types.
* `Registry` is instantiated by passing only a `Config` object to it.

### Migration Steps

1. Remove old references to the old spectator library implementation.
2. Utilize the `Config` & `WriterConfig` to initialize the `Registry`.
3. Currently there is not support to collect runtime metrics for the spectator-cpp library.
4. If you need to configure a `Registry` that doesn't emit metrics, for testing purposes, you can
use the `WriterConfig` to configure a `MemoryWriter`. This will emit metrics to a vector so make
sure to clear the vector every so often.
