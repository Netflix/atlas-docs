The stack language provides some basic techniques to convert an input line into a set of signals
that can be used to trigger and visualize alert conditions. This section assumes a familiarity
with the stack language and the [alerting philosophy](alerting-philosophy.md).

## Signal Line

A signal line is a time series that indicates whether or not a condition is true for a particular
interval. They are modelled by having zero indicate false and non-zero, typically 1, indicating
true. Alerting expressions map some input time series to a set of signal lines that indicate true
when in a triggering state.

## Threshold Alerts

To start we need an input metric. For this example the input will be a sample metric showing
high CPU usage for a period:

@@@ atlas-graph { show-expr=true }
/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum
@@@

Lets say we want to trigger an alert when the CPU usage goes above 80%. To do that simply use the
[:gt](ref/gt.md) operator and append `80,:gt` to the query:

@@@ atlas-graph { show-expr=false }
/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt
@@@

The result is a _signal line_ that is non-zero, typically 1, when in a triggering state and zero
when everything is fine.

## Dampening

Our threshold alert above will trigger if the CPU usage is ever recorded to be above the threshold.
Alert conditions are often combined with a check for the number of occurrences. This is done by
using the [:rolling-count](stateful-rolling-count) operator to get a line showing how many times
the input signal has been true withing a specified window and then applying a second threshold to
the rolling count.

@@@ atlas-example
Input: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt
Rolling Count: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt,5,:rolling-count
Dampened Signal: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt,5,:rolling-count,4,:gt
@@@

## Visualization

A signal line is useful to tell whether or not something is in a triggered state, but can
be difficult for a person to follow. Alert expressions can be visualized by showing the
input, threshold, and triggering state on the same graph.

@@@ atlas-graph { show-expr=true }
/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:2over,:gt,:vspan,40,:alpha,triggered,:legend,:rot,input,:legend,:rot,threshold,:legend,:rot
@@@

## Summary

You should now know the basics of crafting an alert expression using the stack language. Other
topics that may be of interest:

* [Alerting Philosophy](alerting-philosophy.md): overview of best practices associated with alerts.
* [Stack Language Tutorial](tutorial.md): comprehensive list of available operators.
* [DES](des.md): double exponential smoothing. A technique for detecting anomalies in normally clean
  input signals where a precise threshold is unknown. For example, the requests per second hitting
  a service.
