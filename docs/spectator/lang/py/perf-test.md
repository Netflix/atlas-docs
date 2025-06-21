# Performance

## Test Script

Test maximum single-threaded throughput for two minutes.

```python
#!/usr/bin/env python3

import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(thread)d - %(message)s'
)

from spectator import Config, Registry

location = "udp"
# location = "unix"
registry = Registry(Config(location))
# add tags with some length, to simulate more real-world conditions
tags = {"location": location, "version": "correct-horse-battery-staple"}

max_duration = 2 * 60
start = time.perf_counter()

def elapsed():
    return time.perf_counter() - start

print(f"start spectator-py {location} benchmark")
iteration = 1
while elapsed() < max_duration:
    registry.counter("spectator-py.publish", tags).increment()
    if iteration % 500000 == 0:
        print(f"iterations={iteration} elapsed={elapsed():.2f}")
    iteration += 1

print(f"iterations={iteration} elapsed={elapsed():.2f} rate/sec={iteration/elapsed():.2f}")
```

## Results

See [Usage > Performance](usage.md#performance).
