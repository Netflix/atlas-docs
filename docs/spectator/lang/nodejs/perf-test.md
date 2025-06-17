# Performance

## Test Script

Test maximum single-threaded throughput for two minutes.

```javascript
#!/usr/bin/env node

import {Registry} from "nflx-spectator";

// default is udp
const registry = new Registry();
const tags = {"location": "udp", "version": "correct-horse-battery-staple"};

const max_duration = 2 * 60;
const start = performance.now();

function elapsed() {
    return ((performance.now() - start) / 1000).toFixed(2);
}

console.log("start spectator-js udp benchmark");
let iteration = 1;
while (true) {
    // without await, a heap limit allocation fail error will occur around 5.5M iterations (34 sec)
    await registry.counter("spectator-js.publish", tags).increment();
    if (iteration % 500000 === 0) {
        console.log("iterations", iteration, "elapsed", elapsed());
        if (elapsed() > max_duration) {
            break;
        }
    }
    iteration += 1;
}

console.log("iterations", iteration, "rate/sec", iteration/elapsed());
```

## Results

See [Usage > Performance](usage.md#performance).
