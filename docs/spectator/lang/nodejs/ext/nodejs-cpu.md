
Node.js runtime CPU metrics, provided by [spectator-js-nodejsmetrics](../usage.md#spectator-js-nodejsmetrics).

## Metrics

### Common Dimensions

The following dimensions are common to the metrics published by this module:

* `nodejs.version`: The version of the Node.js runtime.

### nodejs.cpuUsage

Percentage of CPU time the Node.js process is consuming, from 0..100.

The usage is divided into the following categories:

* `system`: CPU time spent running the kernel.
* `user`: CPU time spent running user space (non-kernel) processes.

**Unit:** percent

**Dimensions:**

* `id`: The category of CPU usage.

Example:

```json
{
  "tags": {
    "id": "system",
    "name": "nodejs.cpuUsage",
    /// nf.* tags
    "nodejs.version": "v6.5.0"
  },
  "start": 1485813720000,
  "value": 0.8954088417692685
},
{
  "tags": {
    "id": "user",
    "name": "nodejs.cpuUsage",
    /// nf.* tags
    "nodejs.version": "v6.5.0"
  },
  "start": 1485813720000,
  "value": 4.659007745141895
}
```
