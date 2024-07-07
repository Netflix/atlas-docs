The Graph API is the primary means to retrieve data from an Atlas store.

The default response is a PNG image plotting data matching the 
[Atlas Stack Language](../../asl/tutorial.md) expression along with optional parameters 
to control time ranges, size, style, labels, etc. For a quick overview by example see 
the [examples](examples.md) page.

If graphs look familiar, that's because the design and language were inspired by 
[RRDtool](https://oss.oetiker.ch/rrdtool/). RRD style graphs offer concise and highly
customizable views of time series data. While a number of observability tools offer
dynamic charts, a major benefit of these PNG graphs is the ability to snapshot data
in time, particularly when that data may expire from a high throughput data store; 
PNGs are forever. Additionally, the majority of email and on-call systems support 
images out of the box without having to worry about porting a dynamic graphing
library to various browsers and clients.

The API only supports HTTP query strings at this time. This makes it easy to construct
queries with tooling and share the URIs with other users. No JSON request payloads needed.

Additional Output formats, including JSON, can be found in [Outputs](outputs.md).

### URI

`/api/v1/graph?q=<expr>[&OPTIONS]`

### HTTP Method

`GET` - Only the GET method is allowed at this time.

## Query Parameters

### Data

The only required query param is `q` which is the [query expression](../../asl/tutorial.md) 
used by the user to select and manipulate data. The simplest API query you can make is 
`/api/v1/graph?q=42`. This will produce a graph from Atlas with a straight line having a
value of `42` for 3 hours[*](#defaults) with a legend including statistics for the query period. 

All query params related to fetching data:

| Name   | Description           | Default                    | Type                                 |
|--------|-----------------------|----------------------------|--------------------------------------|
| `q`    | Query expression      | must be specified by user  | [expr](../../asl/tutorial.md)               |
| `step` | Step size for data    | auto                       | [duration](../time-parameters.md#durations) |

!!! Warning 
    In most cases users should not set `step` directly. The `step` parameter
    is deprecated.

### Time

There are three parameters to control the time range used for a graph:

| Name   | Description | Default                    | Type |
|--------|-------------|----------------------------|------|
| `s`    | Start time  | `e-3h`[*](#defaults)       | [Time](../time-parameters.md#time)              |
| `e`    | End time    | `now`[*](#defaults)        | [Time](../time-parameters.md#time)              |
| `tz`   | Time zone   | `US/Pacific`[*](#defaults) | [Time zone ID](../time-parameters.md#time-zone) |

For more information on the behavior see the [time parameters](../time-parameters.md) page.

### Image Flags

| Name              | Description                              | Default      | Type                        |
|-------------------|------------------------------------------|--------------|-----------------------------|
| `title`           | Set the graph title                      | no title     | String                      |
| `no_legend`       | Suppresses the legend                    | `0`          | [boolean](#boolean-flags)   |
| `no_legend_stats` | Suppresses summary stats for the legend  | `0`          | [boolean](#boolean-flags)   |
| `axis_per_line`   | Put each line on a separate Y-axis       | `0`          | [boolean](#boolean-flags)   |
| `only_graph`      | Only show the graph canvas               | `0`          | [boolean](#boolean-flags)   |
| `vision`          | Simulate different vision types          | `normal`     | [vision type](vision.md) |

### Image Size

There are four parameters to control the image size and layout used for a graph:

| Name     | Description                                    | Default             | Type                              |
|----------|------------------------------------------------|---------------------|-----------------------------------|
| `layout` | Mode for controlling exact or relative sizing  | `canvas`            | [layout mode](layout.md#modes) |
| `w`      | Width of the canvas or image                   | `700`[*](#defaults) | int                               |
| `h`      | Height of the canvas or image                  | `300`[*](#defaults) | int                               |
| `zoom`   | Transform the size by a zoom factor            | `1.0`               | float                             |

For more information on the behavior see the [graph layout](layout.md) page.

### Y-Axis

| Name             | Description                                        | Default      | Type                               |
|------------------|----------------------------------------------------|--------------|------------------------------------|
| `stack`          | Set the default line style to stack                | `0`          | [boolean](#boolean-flags)          |
| `l`              | Lower bound for the axis                           | `auto-style` | [axis bound](axis-bounds.md)          |
| `u`              | Upper bound for the axis                           | `auto-style` | [axis bound](axis-bounds.md)          |
| `ylabel`         | Label for the axis                                 | no label     | String                             |
| `palette`        | Color palette to use                               | `armytage`   | [palette](color-palettes.md)          |
| `o`              | Use a logarithmic scale (deprecated in 1.6)        | `0`          | [boolean](#boolean-flags)          |
| `scale`          | Set the axis scale to use (since 1.6)              | `linear`     | [scale](axis-scale.md)                |
| `tick_labels`    | Set the mode to use for tick labels                | `decimal`    | [tick label mode](tick.md)     |
| `sort`           | Set the mode to use for sorting the legend         | expr order   | [sort mode](legends.md#sorting-modes) |
| `order`          | Set the order ascending or descending for the sort | `asc`        | [order](legends.md#sorting-order)     |

### Output Format

| Name        | Description                            | Default   | Type                                  |
|-------------|----------------------------------------|-----------|---------------------------------------|
| `format`    | Output format to use                   | `png`     | [output format](outputs.md)       |
| `callback`  | Method name to use for JSONP callback  | none      | String                                |

### Defaults

If marked with an `*` the default shown can be changed by the administrator for the Atlas server. As a result
the default in the table may not match the default you see. The defaults listed do match those used for the
primary Atlas backends in use at Netflix.

For users running their own server, the config settings and corresponding query params are:

| Key                                   | Query Param |
|---------------------------------------|-------------|
| `atlas.webapi.graph.start-time`       | `s`         |
| `atlas.webapi.graph.end-time`         | `e`         |
| `atlas.webapi.graph.timezone`         | `tz`        |
| `atlas.webapi.graph.width`            | `w`         |
| `atlas.webapi.graph.height`           | `h`         |
| `atlas.webapi.graph.palette`          | `palette`   |

### Boolean Flags

Flags with a true or false value are specified using `1` for true and `0` for false.