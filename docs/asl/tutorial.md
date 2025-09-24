Atlas Stack Language is designed to be a stable method of representing complex data queries in
a URL-friendly format. It is loosely based on the
[RPN expressions](http://oss.oetiker.ch/rrdtool/doc/rrdgraph_rpn.en.html) supported by
[Tobias Oetiker](https://tobi.oetiker.ch/hp/)'s [rrdtool](http://oss.oetiker.ch/rrdtool/).
The following is an example of a stack language expression:

`nf.cluster,discovery,:eq,(,nf.zone,),:by`

This example pushes two strings `nf.cluster` and `discovery` onto the stack and then executes the
command `:eq`. The equal command pops two strings from the stack and pushes a query object onto the
stack. The behavior can be described by the stack effect `String:key String:value – Query`. We then
push a list of tag keys to the stack and execute the command `:by` to group the results.

## Parts

There are only four reserved symbols used for structuring the expression: `,:()`

1. Commas separate items on the stack. So `a,b` puts two strings on the stack with values `"a"`
   and `"b"`.
2. Colon is used to prefix operations. If the first character is a colon the item will be treated
   as a command to run. For example, `a,:dup`, will push `"a"` on the stack and then execute the
   [duplicate](./ref/dup.md) operation.
3. Parenthesis are used to indicate the start and end of a list. The expression `(,)` puts an
   empty list on the stack. Commands inside of a list will not be executed unless the list is
   passed to the [call](./ref/call.md) command. For example, `(,:dup,)` will push a list with a single
   string value of `":dup"` on to the stack.

### Escaping Reserved Symbols

When you need to include the reserved symbols `,:()` as literal characters within your data, you can
escape them using Unicode escape sequences. This is useful when working with tag values or string
literals that contain these special characters.

Unicode escape sequences use the format `\uXXXX` where `XXXX` is the four-digit hexadecimal Unicode
code point. For example:

- `,` (comma) can be escaped as `\u002C`
- `:` (colon) can be escaped as `\u003A` 
- `(` (left parenthesis) can be escaped as `\u0028`
- `)` (right parenthesis) can be escaped as `\u0029`

#### Example

Consider a scenario where you want to match a tag value that contains a colon:

```
name,:foo,:eq          # Invalid - colon in :foo is interpreted as a command
name,\u003Afoo,:eq     # Valid - colon is escaped and treated as literal text
```

In the first case, `:foo` would be interpreted as a command, which would cause an error. In the
second case, `\u003Afoo` represents the literal string `:foo`.

#### Preserving Whitespace

Unicode escaping can also be used to preserve whitespace at the beginning and end of tokens,
which is normally trimmed during parsing. This is useful when exact spacing is important for your
data:

```
tag,\u0020value\u0020,:eq    # Preserves leading and trailing spaces around "value"
```

Without escaping, leading and trailing whitespace would be automatically removed from tokens
during parsing.


## Data Model

The stack language is primarily used for representing expressions over tagged time series
data. A tag is a string key value pair used to describe a measurement. Atlas requires at least
one tag with a key of `name`. Example tags represented as a JSON map:

```json
{
  "name":       "jvm.gc.pause",
  "cause":      "Allocation_Failure",
  "statistic":  "count",
  "nf.app":     "www",
  "nf.cluster": "www-main",
  "nf.asg":     "www-main-v001",
  "nf.stack":   "main",
  "nf.node":    "i-01",
  "nf.region":  "us-east-1",
  "nf.zone":    "us-east-1a"
}
```

Typically, tags should be dimensions that allow you to use the name as a pivot and other tags
to drill down into the data. The tag keys are similar to columns in a traditional table, however,
it is important to note that not all time series will have the same set of tag keys.

The tags are used to identify a time series, which conceptually is a set of timestamp value pairs.
Here is a simplified data set shown as a table:

| name        | app   | node   | values                         |
|-------------|-------|--------|--------------------------------|
| cpuUsage    | www   | i-01   | [(05:00, 33.0), (05:01, 31.0)] |
| cpuUsage    | www   | i-02   | [(05:00, 20.0), (05:01, 37.0)] |
| cpuUsage    | db    | i-03   | [(05:00, 57.0), (05:01, 62.0)] |
| diskUsage   | www   | i-01   | [(05:00,  9.0), (05:01,  9.0)] |
| diskUsage   | www   | i-02   | [(05:00,  7.0), (05:01,  8.0)] |
| requestRate | www   |        | [(05:00, 33.0), (05:01, 31.0)] |

The table above will be used for the examples in later sections.

## Simple Expressions

All expressions generally have four parts:

1. **Choosing:** selects a set of time series.
2. **Aggregation:** defines how to combine the selected time series.
3. **Math:** manipulate the time series values or combine aggregated results with binary operations.
4. **Presentation:** adjust how the data is presented in a chart.

### Choosing

The "choosing" or predicate section is used to select a set of time series. The 
primary predicate operators are
[:eq](ref/eq.md) and [:and](ref/and.md).

Sample query to select all time series where the key `node` is equal to `i-01`:

@@@ atlas-stacklang
/api/v1/graph?q=node,i-01,:eq
@@@

If you are familiar with SQL and assume that tag keys are column names, then this would be
equivalent to:

```
select * from time_series where node = 'i-01';
```

Using the [example data set](#data-model) this query would return the following subset:

| name        | app   | node   | values                         |
|-------------|-------|--------|--------------------------------|
| cpuUsage    | www   | i-01   | [(05:00, 33.0), (05:01, 31.0)] |
| diskUsage   | www   | i-01   | [(05:00,  9.0), (05:01,  9.0)] |

To get just the cpu usage for that node, use [:and](ref/and.md):

@@@ atlas-stacklang
/api/v1/graph?q=node,i-01,:eq,name,cpuUsage,:eq,:and
@@@

This would result in:

| name        | app   | node   | values                         |
|-------------|-------|--------|--------------------------------|
| cpuUsage    | www   | i-01   | [(05:00, 33.0), (05:01, 31.0)] |

### Aggregation

An aggregation function maps a set of time series that matched the predicate to a single time series.
Atlas supports four aggregate functions: [sum](ref/sum.md), [min](ref/min.md), [max](ref/max.md), and
[count](ref/count.md). If no aggregate is specified on an expression, then [sum](ref/sum.md) will be
used implicitly.

Using the [example data set](#data-model), these two expressions would be equivalent:

@@@ atlas-stacklang
/api/v1/graph?q=app,www,:eq,name,cpuUsage,:eq,:and
@@@

@@@ atlas-stacklang
/api/v1/graph?q=app,www,:eq,name,cpuUsage,:eq,:and,:sum
@@@

And would result in a single output time series:

| name        | app   | values                         |
|-------------|-------|--------------------------------|
| cpuUsage    | www   | [(05:00, 53.0), (05:01, 68.0)] |

Note that the node is not present in the output. The set of tags on the output will be ones
with exact matches in the predicate clause or explicitly listed in the [group by](#group-by).

If you wanted the max cpu for the application, then you would write:

@@@ atlas-stacklang
/api/v1/graph?q=app,www,:eq,name,cpuUsage,:eq,:and,:max
@@@

What if we want the average? The [count](ref/count.md) aggregate is used to determine how many time
series had a value for a given time. To get the average we divide the sum by the count.

@@@ atlas-stacklang
/api/v1/graph?q=app,www,:eq,name,cpuUsage,:eq,:and,:dup,:sum,:swap,:count,:div
@@@

There is a helper macro [:avg](ref/avg.md) that will do this for you, so you can write:

@@@ atlas-stacklang
/api/v1/graph?q=app,www,:eq,name,cpuUsage,:eq,:and,:avg
@@@

### Group By

In many cases we want to group the results that were selected and return one aggregate per
group. As an example suppose I want to see maximum cpu usage by application:

@@@ atlas-stacklang
/api/v1/graph?q=name,cpuUsage,:eq,:max,(,app,),:by
@@@

Using the [example data set](#data-model), this would result in a two output time series:

| name        | app   | values                         |
|-------------|-------|--------------------------------|
| cpuUsage    | www   | [(05:00, 33.0), (05:01, 37.0)] |
| cpuUsage    | db    | [(05:00, 57.0), (05:01, 62.0)] |

### Math

Once you have a set of lines, it can be useful to manipulate them. The supported operations
generally fall into two categories: unary operations to alter a single time series and binary
operations that combine two time series.

Examples of unary operations are [negate](ref/neg.md) and [absolute value](ref/abs.md). To apply
the absolute value:

@@@ atlas-stacklang
/api/v1/graph?q=app,web,:eq,name,cpu,:eq,:and,:sum,:abs
@@@

Multiple operations can be applied, for example, negating the line then applying the absolute
value:

@@@ atlas-stacklang
/api/v1/graph?q=app,web,:eq,name,cpu,:eq,:and,:sum,:neg,:abs
@@@

Common binary operations are [add](ref/add.md), [subtract](ref/sub.md), [multiply](ref/mul.md), and
[divide](ref/div.md). The [aggregation section](#aggregation) has an example of using divide to
compute the average.

### Presentation

Once you have a final expression, you can apply presentation settings to alter how a time
series is displayed in the chart. One of the most common examples is setting the label
to use for the [legend](ref/legend.md):

@@@ atlas-stacklang
/api/v1/graph?q=app,www,:eq,name,cpuUsage,:eq,:and,:avg,average+cpu+usage,:legend
@@@

You can also use tag keys as variables in the legend text, for example, setting the legend to
the application:

@@@ atlas-stacklang
/api/v1/graph?q=app,www,:eq,name,cpuUsage,:eq,:and,:avg,(,app,),:by,$(app),:legend
@@@

It is also common to adjust the how the lines are shown. For example, to stack each of the lines
we can use the [:stack](ref/stack.md) command to adjust the line style:

@@@ atlas-stacklang
/api/v1/graph?q=app,www,:eq,name,cpuUsage,:eq,:and,:avg,(,app,),:by,:stack,$(app),:legend
@@@
