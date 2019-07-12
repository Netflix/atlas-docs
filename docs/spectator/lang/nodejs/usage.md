## Project

### spectator-js

[![Build Status](https://travis-ci.org/Netflix/spectator-js.svg?branch=master)](https://travis-ci.org/Netflix/spectator-js) 
[![codecov](https://codecov.io/gh/Netflix/spectator-js/branch/master/graph/badge.svg)](https://codecov.io/gh/Netflix/spectator-js)

* [Source](https://github.com/Netflix/spectator-js)
* [NPM](https://www.npmjs.com/package/nflx-spectator)
* **Product Lifecycle:** GA
* **Module Name:** `nflx-spectator`

This module can be used to instrument an application using counters, distribution summaries,
gauges, long task timers, timers, and more complex meter types (like Bucket or Percentile
Timers) using a dimensional data model.

The generated metrics are periodically sent to an [Atlas] Aggregator.

[spectator-js]: #spectator-js
[Atlas]: https://github.com/Netflix/atlas

### spectator-js-nodejsmetrics

[![Build Status](https://travis-ci.org/Netflix-Skunkworks/spectator-js-nodejsmetrics.svg?branch=master)](https://travis-ci.org/Netflix-Skunkworks/spectator-js-nodejsmetrics) 
[![codecov](https://codecov.io/gh/Netflix-Skunkworks/spectator-js-nodejsmetrics/branch/master/graph/badge.svg)](https://codecov.io/gh/Netflix-Skunkworks/spectator-js-nodejsmetrics)

* [Source](https://github.com/Netflix-Skunkworks/spectator-js-nodejsmetrics)
* [NPM](https://www.npmjs.com/package/nflx-spectator-nodejsmetrics)
* **Product Lifecycle:** GA
* **Module Name:** `nflx-spectator-nodejsmetrics`

Generate Node.js runtime metrics using the [spectator-js] Node module.

[spectator-js-nodejsmetrics]: #spectator-js-nodejsmetrics

## Install Libraries

Add the following dependencies to `package.json`:

```json
{
  "dependencies": {
    "nflx-spectator": "*",
    "nflx-spectator-nodejsmetrics": "*"
  }
}
```

## Instrumenting Code

```javascript
'use strict';

const spectator = require('nflx-spectator');

// Netflix applications can use the nflx-spectator-config node module available
// internally through artifactory to generate the config required by nflx-spectator
function getConfig() {
  return {
    commonTags: {'nf.node': 'i-1234'},
    uri: 'http://atlas.example.org/v1/publish',
    timeout: 1000 // milliseconds 
  }
}

class Response {
  constructor(status, size) {
    this.status = status;
    this.size = size;
  }
}

class Server {
  constructor(registry) {
    this.registry = registry;
    // create a base Id, to which we'll add some dynamic tags later
    this.requestCountId = registry.createId('server.requestCount', {version: 'v1'});
    this.requestLatency = registry.timer('server.requestLatency');
    this.responseSize = registry.distributionSummary('server.responseSizes');
  }
  
  handle(request) {
    const start = this.registry.hrtime();
    
    // do some work based on request and obtain a response
    const res = new Response(200, 64);
    
    // update the counter id with dimensions based on the request. The
    // counter will then be looked up in the registry which should be 
    // fairly cheap, such as a lookup of an id object in a map
    // However, it is more expensive than having a local variable set
    // to the counter
    const counterId = this.requestCountId.withTags({country: request.country, 
        status: res.status});
    this.registry.counter(counterId).increment();
    this.requestLatency.record(this.registry.hrtime(start));
    this.responseSize.record(res.size);
    return res;
  }
}

const config = getConfig();
const registry = new spectator.Registry(config);

class Request {
  constructor(country) {
    this.country = country;
  }
}

// somehow get a request from the user...
function getNextRequest() {
  return new Request('AR');
}

function handleTermination() {
  registry.stop();
}

process.on('SIGINT', handleTermination);
process.on('SIGTERM', handleTermination);

registry.start();

const server = new Server(registry);

for (let i = 0; i < 3; ++i) {
  const req = getNextRequest();
  server.handle(req)
}

registry.stop();
```

## Enable Runtime Metrics

```javascript
'use strict';

function getConfig() {
}

const spectator = require('nflx-spectator');
const NodeMetrics = require('nflx-spectator-nodejsmetrics');

const config = {
  commonTags: {'nf.node': 'i-1234'},
  uri: 'http://atlas.example.org/v1/publish'
};
const registry = new spectator.Registry(config);
registry.start();

const metrics = new NodeMetrics(registry);
metrics.start(); // start collecting nodejs metrics

// ...

metrics.stop();
registry.stop();
```

## Netflix Integration

Create a Netflix Spectator Config to be used by [spectator-js].

Only applications should depend on the `nflx-spectator-jsconf` package. Libraries should get the
Registry passed by the application, and therefore should only need to depend on [spectator-js].

Add the following dependencies to `package.json`:

```json
{
  "dependencies": {
    "nflx-spectator": "*",
    "nflx-spectator-nodejsmetrics": "*",
    "nflx-spectator-jsconf": "*"
  }
}
```

This configuration also brings in [spectator-js-nodejsmetrics] to provide Node.js runtime metrics.

You can override the logger used by the Spectator registry by setting the logger property. The
specified logger should provide `debug`, `info`, and `error` methods. By default, [spectator-js]
logs to stdout.

```js
const spectator = require('nflx-spectator');
const NodeMetrics = require('nflx-spectator-nodejsmetrics');
const getSpectatorConfig = require('nflx-spectator-jsconf');
const logger = require('pino')();

//...

const registry = new spectator.Registry(getSpectatorConfig());
registry.logger = logger;
registry.start();

const metrics = new NodeMetrics(registry);
metrics.start();

function handleTermination() {
  metrics.stop();
  registry.stop();
}

process.on('SIGINT', handleTermination);
process.on('SIGTERM', handleTermination);

//... your app

handleTermination();
```
