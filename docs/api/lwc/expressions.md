This page is a reference for the LWC streams summary endpoint provided by the LWC API.
The endpoint is useful for debugging streams attached to a particular LWC instance. It does
not list streams for an entire cluster.

### URI

`/lwc/api/v1/expressions[/<cluster>]`

## Header Parameters

### `If-None-Match`
Optional hex encoded CRC-32 signature of the expressions set used to determine if the
set is the same across nodes in a cluster. If the signature matches, a 304 Not Modified
response is returned. If the signature does not match, the full expression set is returned
with a 200 status code.

## Query Parameters

### None

Returns a list of all expressions under evaluation by the cluster.

**Response:**
```json
{
  "expressions": [{
    "expression": "nf.region,us-east-1,:eq,nf.cluster,testcluster,:eq,:and,name,cpuALL.stolen,:eq,:and,:sum,(,nf.node,),:by",
    "frequency": 60000,
    "id": "c80bebe3cd68fd1828f627d279584c7891162aa0"
  }, {
    "expression": "nf.app,testapp,:eq,error,400,:eq,:and,name,downstreamErrors,:eq,:and,:sum",
    "frequency": 60000,
    "id": "29b77f4d9c156a8db7db8d642f1ead63fc610887"
  }]
}
```

### Cluster

Returns a list of evaluated expressions that could match on the given predicate. The
predicate may be a literal cluster name matching an `nf.cluster` value or it may be a
Netflix standardized auto scaling group name, security group name or load balancer name
wherein `nf.cluster`, `nf.app` and `nf.stack` could be parsed and applied as a filter.

**Response:**
Filtered response of the main expression set.
