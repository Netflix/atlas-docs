@@@ atlas-signature
replacement: String
searchPattern: String
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Perform search and replace operations on legend text using regular expressions. This operator
provides powerful text transformation capabilities similar to the global search and replace
operations found in text editors and command-line tools like `sed` or `vim`.

## Parameters

* **expr**: The time series expression whose legend text will be modified
* **searchPattern**: Regular expression pattern to search for in the legend text
* **replacement**: Replacement text that can include capture group references

## Pattern Syntax

The search pattern uses standard regular expression syntax with support for:

* **Literal text**: Direct string matching (e.g., `nccp-` matches the literal text "nccp-")
* **Character classes**: `[a-z]` matches any lowercase letter
* **Anchors**: `^` (start of string), `$` (end of string)
* **Quantifiers**: `*` (zero or more), `+` (one or more), `?` (zero or one)
* **Grouping**: `(...)` creates capture groups for use in replacement

## Replacement Variables

The replacement string supports variable substitution using the same syntax as [:legend](legend.md):

### Capture Group References
* **Numbered groups**: `$1`, `$2`, etc. refer to capture groups by position
* **Named groups**: `$name` refers to named capture groups like `(?<name>...)`

### Standard Variables
* **Tag values**: `$tagname` substitutes tag values from the time series
* **Special variables**: `$atlas.offset` and other system variables

## Examples

### Removing Prefixes

Remove the "nccp-" prefix from cluster names:

@@@ atlas-example { hilite=:s }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend,^nccp-(.*)$,$1,:s
@@@

### Named Capture Groups

Using named groups for clearer replacement patterns:

@@@ atlas-example { hilite=:s }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend,^nccp-(?<stack>.*)$,$stack,:s
@@@

### Simple Text Replacement

Replace literal text without regex patterns:

@@@ atlas-example { hilite=:s }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend,nccp-,_,:s
@@@

### Pattern-Based Transformation

Transform character patterns with replacement:

@@@ atlas-example { hilite=:s }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend,([a-z]),_$1,:s
@@@

## Processing Order

When applied to time series with multiple legend values, the search and replace operation
is performed independently on each legend string. The operation affects only the display
text and does not modify the underlying tag values.

## Related Operations

* [:legend](legend.md) - Set custom legend text with variable substitution
* [:decode](decode.md) - Decode encoded characters in legend text
* [:as](as.md) - Rename tag keys for mathematical operations
* [:format](format.md) - Create formatted strings with printf-style patterns

Since: 1.6