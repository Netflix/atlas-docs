## Project

[![Build Status](https://travis-ci.org/Netflix/spectator-py.svg?branch=master)](https://travis-ci.org/Netflix/spectator-py) 

* [Source](https://github.com/Netflix/spectator-py)
* [PyPI](https://pypi.org/project/netflix-spectator-py/)
* **Product Lifecycle:** Beta
* **Module Name:** netflix-spectator-py

This module can be used to instrument an application using Counters, Distribution Summaries,
Gauges, Timers, and Percentile Timers using a dimensional data model.

The generated metrics are periodically sent to an [Atlas] Aggregator.

[Atlas]: https://github.com/Netflix/atlas

## Install Library

Install the library from PyPI:

```shell
pip install netflix-spectator-py
```

## Instrumenting Code

```python
from spectator import GlobalRegistry

GlobalRegistry.counter('server.numRequests').increment()
GlobalRegistry.gauge('server.capacity').set(50)
```

## Usage

The import of the` GlobalRegistry` will start a daemon thread that will publish metrics in the
background. The cache will be flushed upon normal interpreter termination using [atexit], with
the following exceptions:

* The program is killed by a signal not handled by Python.
* A Python fatal internal error is detected.
* When `os._exit()` is called.

[atexit]: https://docs.python.org/3.7/library/atexit.html

If you do not want the `GlobalRegistry` to automatically start at module import, then set the
following environment variable:

```shell
SPECTATOR_PY_DISABLE_AUTO_START_GLOBAL=1
```

With this configuration, you will have to manually call the `GlobalRegistry.start()` and
`GlobalRegistry.stop()` methods. Failure to do so will prevent metric publishing.

### Common Tagging 

This library does not add the `nf.node` tag to the published metrics. If you need it, remember to
add it.

### Gunicorn Preload

If you are using this library while running behind Gunicorn, make sure that you do not use 
the `--preload` flag, because it can cause issues with how the background thread operates due
to loading the application code before the worker processes are forked.

On the Paved Path, with EzConfig, that is achieved with the following configuration:

```ini
WSGI_GUNICORN_PRELOAD = undef
```

## Netflix Integration

Add the internal configuration for the Spectator Python client, so that it can send metrics to
an [Atlas] Aggregator cluster. Replace `SMARTIPROXY_HOSTNAME` with the hostname of the internal
SmartiProxy service.

```
pip install -i https://SMARTIPROXY_HOSTNAME/pypi netflix-spectator-pyconf
```
