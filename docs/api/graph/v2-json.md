The `v2.json` output format returns a JSON array of typed objects that fully describe a graph.
Each object has a `type` field used to determine how it should be interpreted. The overall
structure is:

```
[graph-image?, graph-metadata, plot-metadata*, heatmap*, data*]
```

Metadata objects are emitted first so a consumer can set up rendering before data arrives.
Data entries (`timeseries`, `hspan`, `vspan`, `message`) reference a plot by its index. This
design allows data to be streamed incrementally as it becomes available.

All numeric values that are not valid JSON numbers (e.g., `NaN`, `Infinity`) are quoted as
strings so the output is parseable with any standard JSON parser.

Colors are encoded as 8-character hex strings in `RRGGBBAA` format (e.g., `"f423271a"`).

## graph-image

An optional pre-rendered PNG image of the graph encoded as a
[data URI](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs).
This can be used for partially dynamic views where the static image is shown first while
a richer rendering is prepared. This entry is suppressed when the `no-image` rendering hint
is set.

| Field  | Type   | Description |
|--------|--------|-------------|
| `type` | string | Always `"graph-image"`. |
| `data` | string | Data URI with a base64-encoded PNG, e.g., `"data:image/png;base64,..."`. |

Example:

```json
{
  "type": "graph-image",
  "data": "data:image/png;base64,iVBORw0KGgo..."
}
```

## graph-metadata

Top-level metadata describing the time range, dimensions, and display settings of the graph.
Exactly one `graph-metadata` object is present in the output.

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"graph-metadata"`. |
| `startTime` | number | Start of the time range in epoch milliseconds. |
| `endTime` | number | End of the time range in epoch milliseconds. |
| `timezones` | string[] | List of [timezone](time-zone.md) IDs used for rendering (e.g., `["US/Eastern"]`). |
| `step` | number | Step size in milliseconds between data points. |
| `width` | number | Width of the graph in pixels. |
| `height` | number | Height of the graph in pixels. |
| `layout` | string | [Layout](layout.md) mode. See [Layout values](#layout-values). |
| `zoom` | number | Zoom factor applied to the graph. |
| `title` | string? | Optional title displayed above the graph. |
| `legendType` | string | [Legend](legends.md) display mode. See [LegendType values](#legendtype-values). |
| `onlyGraph` | boolean | If `true`, only the graph area is rendered (no axes, legend, etc.). |
| `theme` | string | [Theme](theme.md) name, e.g., `"light"` or `"dark"`. |
| `loadTime` | number? | Time in milliseconds to load the data. Omitted if not measured. |
| `stats` | object? | Collector statistics. See [Stats object](#stats-object). Omitted if unknown. |
| `warnings` | string[] | List of warning messages generated during evaluation. |
| `renderingHints` | string[]? | Optional set of rendering hints. Omitted when empty. |

Example:

```json
{
  "type": "graph-metadata",
  "startTime": 1325408160000,
  "endTime": 1325408460000,
  "timezones": ["UTC"],
  "step": 60000,
  "width": 700,
  "height": 300,
  "layout": "CANVAS",
  "zoom": 1.0,
  "legendType": "LABELS_WITH_STATS",
  "onlyGraph": false,
  "theme": "light",
  "warnings": []
}
```

### Stats object

| Field | Type | Description |
|-------|------|-------------|
| `inputLines` | number | Number of input time series before any filtering. |
| `inputDatapoints` | number | Number of input data points. |
| `outputLines` | number | Number of output time series after filtering. |
| `outputDatapoints` | number | Number of output data points. |

### Layout values

| Value | Description |
|-------|-------------|
| `CANVAS` | Default. The width and height define the canvas area. |
| `IMAGE` | The width and height define the full image including axes and legends. |
| `IMAGE_WIDTH` | Only the width is fixed to the image size; height follows the canvas. |
| `IMAGE_HEIGHT` | Only the height is fixed to the image size; width follows the canvas. |

### LegendType values

| Value | Description |
|-------|-------------|
| `OFF` | No legend is shown. |
| `LABELS_ONLY` | Shows legend labels without summary statistics. |
| `LABELS_WITH_STATS` | Default. Shows legend labels with summary statistics. |

## plot-metadata

Metadata for a single Y-axis (plot). There is one `plot-metadata` object per plot, supporting
[multi-Y-axis](multi-y.md) configurations. Lines and annotations reference a plot by its `id`.

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"plot-metadata"`. |
| `id` | number | Zero-based index of this plot. Referenced by data entries via `plot`. |
| `ylabel` | string? | Optional label for the Y-axis. |
| `axisColor` | string? | Optional color for the axis in `RRGGBBAA` hex format. |
| `scale` | string | Y-axis [scale](axis-scale.md). See [Scale values](#scale-values). |
| `upper` | string | Upper [bound](axis-bounds.md) for the Y-axis. See [Bound values](#bound-values). |
| `lower` | string | Lower [bound](axis-bounds.md) for the Y-axis. See [Bound values](#bound-values). |
| `tickLabelMode` | string | Format for [tick labels](tick.md). See [TickLabelMode values](#ticklabelmode-values). |

Example:

```json
{
  "type": "plot-metadata",
  "id": 0,
  "scale": "LINEAR",
  "upper": "auto-style",
  "lower": "auto-style",
  "tickLabelMode": "DECIMAL"
}
```

### Scale values

| Value | Description |
|-------|-------------|
| `LINEAR` | Default. Linear scale. |
| `LOGARITHMIC` | Logarithmic scale. |
| `LOG_LINEAR` | Logarithmic for large values, linear near zero. |
| `POWER_2` | Power of 2 scale. |
| `SQRT` | Square root scale. |

### Bound values

Plot bounds are represented as strings. Possible values:

| Value | Description |
|-------|-------------|
| `"auto-style"` | Default. Automatically determined based on the line style. |
| `"auto-data"` | Automatically determined based on the data range. |
| A number string, e.g., `"42.0"` | Explicit fixed bound. |

### TickLabelMode values

| Value | Description |
|-------|-------------|
| `OFF` | No tick labels. |
| `DECIMAL` | Default. Standard decimal notation. |
| `BINARY` | Binary (power of 2) notation, e.g., Ki, Mi, Gi. |
| `DURATION` | Values formatted as durations. |

## timeseries

A time series line with its data and display properties.

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"timeseries"`. |
| `id` | string? | Optional identifier computed from the tags and query. |
| `plot` | number | Index of the plot this line belongs to. |
| `label` | string | Display label for the line. |
| `color` | string | Line [color](color-palettes.md) in `RRGGBBAA` hex format. |
| `lineStyle` | string | How the line is drawn. See [LineStyle values](#linestyle-values) and [Line Styles](line-styles.md). |
| `lineWidth` | number | Width of the line in pixels. See [Line Attributes](line-attributes.md). |
| `query` | string? | Optional original query expression that produced this line. |
| `groupByKeys` | string[]? | Keys used for group by, if applicable. Omitted when empty. |
| `tags` | object | Tag key-value pairs for this time series. |
| `data` | object | The data payload. See [Data object](#data-object). |

Example:

```json
{
  "type": "timeseries",
  "plot": 0,
  "label": "hourOfDay",
  "color": "f4232700",
  "lineStyle": "LINE",
  "lineWidth": 1.0,
  "tags": {
    "name": "hourOfDay"
  },
  "data": {
    "type": "array",
    "values": [8.0, 8.0, 8.0, 8.0, 9.0]
  }
}
```

### LineStyle values

| Value | Description |
|-------|-------------|
| `LINE` | Default line rendering. |
| `AREA` | Filled area from the line to zero. |
| `STACK` | Stacked area, layered on top of previous stacked lines. |
| `VSPAN` | Vertical span highlighting. |
| `HEATMAP` | Rendered as a heatmap. |

### Data object

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | `"array"` for time series data. |
| `values` | number[] | Array of data point values, one per step from `startTime` to `endTime`. Non-numeric values like `NaN` are quoted as strings. |

## hspan

A horizontal span annotation — a shaded horizontal band across the graph between two
Y-axis values.

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"hspan"`. |
| `plot` | number | Index of the plot this span belongs to. |
| `label` | string? | Optional display label. |
| `color` | string | Fill color in `RRGGBBAA` hex format. |
| `v1` | number | Lower Y-axis bound of the span. |
| `v2` | number | Upper Y-axis bound of the span. |

Example:

```json
{
  "type": "hspan",
  "plot": 0,
  "color": "e7298a1a",
  "v1": 30.0,
  "v2": 60.0
}
```

## vspan

A vertical span annotation — a shaded vertical band across the graph between two
points in time.

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"vspan"`. |
| `plot` | number | Index of the plot this span belongs to. |
| `label` | string? | Optional display label. |
| `color` | string | Fill color in `RRGGBBAA` hex format. |
| `t1` | number | Start time in epoch milliseconds. |
| `t2` | number | End time in epoch milliseconds. |

Example:

```json
{
  "type": "vspan",
  "plot": 0,
  "color": "e7298a1a",
  "t1": 1325408200000,
  "t2": 1325408300000
}
```

## message

A text message associated with a plot, typically used for warnings or informational
annotations.

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"message"`. |
| `plot` | number | Index of the plot this message belongs to. |
| `label` | string | The message text. |
| `color` | string | Color in `RRGGBBAA` hex format. |

Example:

```json
{
  "type": "message",
  "plot": 0,
  "label": "NO DATA",
  "color": "ff000000"
}
```

## heatmap

[Heatmap](heatmap.md) data for a plot. Contains bucket definitions, a color palette mapping,
and the cell counts.

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"heatmap"`. |
| `plot` | number | Index of the plot this heatmap belongs to. |
| `colorScale` | string | Scale used for mapping counts to colors. Uses [Scale values](#scale-values). |
| `upper` | string | Upper bound. Uses [Bound values](#bound-values). |
| `lower` | string | Lower bound. Uses [Bound values](#bound-values). |
| `label` | string? | Optional label for the heatmap. |
| `yTicks` | object[] | Y-axis bucket boundaries. See [yTick object](#ytick-object). |
| `colorTicks` | object[] | Color mapping boundaries. See [colorTick object](#colortick-object). |
| `data` | object | Cell count data. See [Heatmap data object](#heatmap-data-object). |

### yTick object

Defines the vertical buckets for heatmap counts.

| Field | Type | Description |
|-------|------|-------------|
| `min` | number | Lower bound of the bucket. |
| `max` | number | Upper bound of the bucket. |
| `label` | string | Display label for this tick. |

### colorTick object

Defines the mapping from counts to colors.

| Field | Type | Description |
|-------|------|-------------|
| `color` | string | Color in `RRGGBBAA` hex format. |
| `min` | number | Minimum count for this color range. |
| `max` | number | Maximum count for this color range. |
| `label` | string | Display label for this color range. |

### Heatmap data object

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Always `"heatmap"`. |
| `values` | number[][] | 2D array of counts. Outer array is one entry per time step, inner array is one count per Y-axis bucket. |
