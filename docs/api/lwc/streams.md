This page is a reference for the LWC streams summary endpoint provided by the LWC API.
The endpoint is useful for debugging streams attached to a particular LWC instance. It does
not list streams for an entire cluster.

### URI

`/api/v1/streams[/<streamID>]`

## Query Parameters

### None

When called without a stream ID path, a list of active stream summaries are returned, e.g. 

**Response:**
```json
[{
	"streamId": "96a784fe-e335-4e76-b3d4-d7b401f65e16",
	"remoteAddress": "127.0.0.1:54065",
	"receivedMessages": {
		"current": 50
	},
	"droppedMessages": {
		"current": 0
	}
}, {
	"streamId": "a5f83589-bf3f-4692-9e28-df47dfe8333c",
	"remoteAddress": "127.0.0.1:53109",
	"receivedMessages": {
		"current": 128
	},
	"droppedMessages": {
		"current": 0
	}
}]
```

The `receivedMessages` and `droppedMessages` represent the number of messages in current
minute interval (not the lifetime of the stream).

### Stream ID

Returns a summary and the list of expressions the stream is subscribed to given an active 
stream ID. For example, `/api/v1/streams/96a784fe-e335-4e76-b3d4-d7b401f65e16`

**Response:**
```json
{
	"metadata": {
		"streamId": "96a784fe-e335-4e76-b3d4-d7b401f65e16",
		"remoteAddress": "127.0.0.1:54065",
		"receivedMessages": {
			"current": 1092
		},
		"droppedMessages": {
			"current": 0
		}
	},
	"subscriptions": [{
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
The `receivedMessages` and `droppedMessages` represent the number of messages in current
minute interval (not the lifetime of the stream). `subscriptions` is the list of expressions,
their ID and step size (frequency at which data is emitted).
