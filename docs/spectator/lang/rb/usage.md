## Project

[![Build Status](https://travis-ci.org/Netflix/spectator-rb.svg?branch=master)](https://travis-ci.org/Netflix/spectator-rb) 

* [Source](https://github.com/Netflix/spectator-rb)
* [RubyGems](https://rubygems.org/gems/netflix-spectator-rb)
* **Product Lifecycle:** Alpha
* **Module Name:** `netflix-spectator-rb`

This implements a basic [Spectator](https://github.com/Netflix/spectator) library for instrumenting
Ruby applications, sending metrics to an [Atlas] aggregator service.

[Atlas]: https://github.com/Netflix/atlas

## Install Library

Install the library from RubyGems:

```shell
gem install spectator-rb
```

## Instrumenting Code

```ruby
require 'spectator'

class Response
  attr_accessor :status, :size

  def initialize(status, size)
    @status = status
    @size = size
  end
end

class Request
  attr_reader :country

  def initialize(country)
    @country = country
  end
end

class ExampleServer
  def initialize(registry)
    @registry = registry
    @req_count_id = registry.new_id('server.requestCount')
    @req_latency = registry.timer('server.requestLatency')
    @resp_sizes = registry.distribution_summary('server.responseSizes')
  end

  def expensive_computation(request)
    # ...
  end

  def handle_request(request)
    start = @registry.clock.monotonic_time

    # initialize response
    response = Response.new(200, 64)

    # Update the counter id with dimensions based on the request. The
    # counter will then be looked up in the registry which should be
    # fairly cheap, such as lookup of id object in a map
    # However, it is more expensive than having a local variable set
    # to the counter.
    cnt_id = @req_count_id.with_tag(:country, request.country)
                          .with_tag(:status, response.status.to_s)
    @registry.counter_with_id(cnt_id).increment

    # ...
    @req_latency.record(@registry.clock.monotonic_time - start)
    @resp_sizes.record(response.size)

    # timers can also time a given block
    # this is equivalent to:
    #  start = @registry.clock.monotonic_time
    #  expensive_computation(request)
    #  @registry.timer('server.computeTime').record(@registry.clock.monotonic_time - start)
    @registry.timer('server.computeTime').time { expensive_computation(request) }
    # ...
  end
end

config = {
  common_tags: { :'nf.app' => 'foo' },
  frequency: 0.5,
  uri: 'http://localhost:8080/api/v4/publish'
}

registry = Spectator::Registry.new(config)
registry.start

server = ExampleServer.new(registry)

# ...
# process some requests
requests = [Request.new('us'), Request.new('ar'), Request.new('ar')]
requests.each { |req| server.handle_request(req) }
sleep(2)

registry.stop
```

## Netflix Integration

Add the internal configuration for the Spectator Ruby client, so that it can send metrics to
an [Atlas] Aggregator cluster.

If you are using the internal Artifactory, add the dependency to your Gemfile:

```ruby
gem 'netflix-spectator-config'
gem 'netflix-spectator-rb'
```

If you are not using the internal Artifactory, then you can do the following, replacing
`STASH_HOSTNAME_AND_PORT` with appropriate values:

```ruby
gem 'netflix-spectator-config', git: 'ssh://git@STASH_HOSTNAME_AND_PORT/cldmta/nflx-spectator-rb.git'
gem 'netflix-spectator-rb'
```

Once the configuration Gem is installed, it is used as follows:

```ruby
require 'spectator_config'
require 'spectator'

config = SpectatorConfig.config
registry = Spectator::Registry.new(config)
registry.start

# ...

registry.stop
```
