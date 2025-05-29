from typing import List

options_single: str = 'show-expr=true'
options_multiple: str = 'show-expr=true something-else=false'
options_no_equals = 'show-expr true'
options_unencoded_equals = 'hilite=&l=0'
options_encoded_equals = 'hilite=&l%3d0 something-else=&l%3D0'

atlas_example_start_line: str = '<p>@@@ atlas-example'

atlas_example_line: str = 'Dampened Signal: /api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt,5,:rolling-count,4,:gt'

atlas_graph_start_line: str = '<p>@@@ atlas-graph { show-expr=true }'

atlas_graph_line: str = '/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum'

atlas_stacklang_start_line: str = '<p>@@@ atlas-stacklang'

atlas_stacklang_line: str = '/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum'

atlas_uri_start_line: str = '<p>@@@ atlas-uri'

atlas_uri_line: str = '/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum'

invalid_start_line: str = '<p>@@@ foo-block'

block_query_patterns: List[str] = [
    '/api/v1/graph?q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100',
    '/api/v1/graph?s=e-3h&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum&e=2012-01-01T07:00&tz=UTC&l=0&h=100',
    '/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum'
]

graph_image_html_template: str = """\
<html>

<style>
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>

<img src="IMG_SRC" width="IMG_WIDTH" height="IMG_HEIGHT"/>

</html>
"""

alerting_expressions: str = """\
<p>The stack language provides some basic techniques to convert an input line into a set of signals
that can be used to trigger and visualize alert conditions. This section assumes a familiarity
with the stack language and the <a href="Alerting-Philosophy">alerting philosophy</a></p>
<h2 id="threshold-alerts">Threshold Alerts<a class="headerlink" href="#threshold-alerts" title="Permanent link">&para;</a></h2>
<p>To start we need an input metric. For this example the input will be a sample metric showing
high CPU usage for a period:</p>
<p>@@@ atlas-graph { show-expr=true }
/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum
@@@</p>
<p>Lets say we want to trigger an alert when the CPU usage goes above 80%. To do that simply use the
<a href="math-gt">:gt</a> operator and append <code>80,:gt</code> to the query:</p>
<p>@@@ atlas-graph { show-expr=true }
/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt
@@@</p>
<p>The result is a <em>signal line</em> that is non-zero, typically 1, when in a triggering state and zero
when everything is fine.</p>
<h2 id="dampening">Dampening<a class="headerlink" href="#dampening" title="Permanent link">&para;</a></h2>
<p>Our threshold alert above will trigger if the CPU usage is ever recorded to be above the
threshold. Alert conditions are often combined with a check for the number of occurrences. This
is done by using the <a href="stateful-rolling-count">:rolling-count</a> operator to get a line showing
how many times the input signal has been true withing a specified window and then applying a
second threshold to the rolling count.</p>
<p>@@@ atlas-example
Input: /api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt
Rolling-count: /api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt,5,:rolling-count
Dampened signal: /api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:gt,5,:rolling-count,4,:gt
@@@</p>
<h2 id="visualization">Visualization<a class="headerlink" href="#visualization" title="Permanent link">&para;</a></h2>
<p>A signal line is useful to tell whether or not something is in a triggered state, but can
be difficult for a person to follow. Alert expressions can be visualized by showing the
input, threshold, and triggering state on the same graph.</p>
<p>@@@ atlas-graph { show-expr=true }
/api/v1/graph?s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&h=100&q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:and,:sum,80,:2over,:gt,:vspan,40,:alpha,triggered,:legend,:rot,input,:legend,:rot,threshold,:legend,:rot
@@@</p>
<h2 id="summary">Summary<a class="headerlink" href="#summary" title="Permanent link">&para;</a></h2>
<p>You should now know the basics of crafting an alert expression using the stack language. Other
topics that may be of interest:</p>
<ul>
<li><a href="Alerting-Philosophy">Alerting Philosophy</a>: overview of best practices associated with alerts.</li>
<li><a href="Stack-Language-Reference">Stack Language Reference</a>: comprehensive list of avialable operators.</li>
<li><a href="DES">DES</a>: double exponential smoothing. A technique for detecting anomalies in normally clean
  input signals where a precise threshold is unknown. For example, the requests per second hitting
  a service.</li>
</ul>
"""
