@@@ atlas-signature
args: List
pattern: String
-->
str: String
@@@

Format a string using printf-style formatting patterns. This allows for dynamic string
construction by substituting values from a list into placeholders in a format string.

## Parameters

* **pattern**: A string containing format specifiers (e.g., `%s`, `%d`, `%f`)
* **args**: A list of values to substitute into the format placeholders

## Format Specifiers

Common format specifiers supported:
* `%s` - String representation of any object
* `%d` - Decimal integer
* `%f` - Floating point number
* `%x` - Hexadecimal representation
* `%%` - Literal percent sign

For complete formatting options, see the [Java Formatter][formatter] documentation.

[formatter]: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Formatter.html

## Examples

Basic string substitution:

@@@ atlas-stacklang
/api/v1/graph?q=foo%s,(,bar,),:format
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>List(bar)</td>
<td>foobar</td>
</tr><tr>
<td>1</td>
<td>foo%s</td>
<td></td>
</tr></tbody></table>

This substitutes the string "bar" from the list into the `%s` placeholder in "foo%s",
resulting in "foobar".

## Related Operations

* [:list](list.md) - Create lists of arguments for formatting
* [:legend](legend.md) - Custom legend formatting (often uses formatted strings)
* [:get](get.md) - Retrieve values that can be used in format arguments
* [:map](map.md) - Apply formatting to multiple items