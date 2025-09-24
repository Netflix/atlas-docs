@@@ atlas-signature
format: String
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Decode encoded characters in legend text for improved presentation. This operator reverses
the encoding that clients often apply to tag values when special characters need to be
transmitted safely in URIs. It's primarily used for making legends more readable by
converting encoded symbols back to their original form.

!!! warning
    **Use Sparingly**: Avoid encoding structural information into tag values. This feature
    should be used carefully to prevent combinatorial explosion of tag combinations.

## Parameters

* **expr**: The time series expression whose legend text will be decoded
* **format**: The decoding format to apply (`none` or `hex`)

## Decoding Formats

### `none` (Default)
* **Behavior**: No modification to legend strings
* **Use case**: When no decoding is needed or to explicitly disable decoding

### `hex` (Hex Decoding)
* **Behavior**: Decodes hex-encoded characters using `_` as the escape prefix
* **Format**: Similar to [URL encoding](https://en.wikipedia.org/wiki/Percent-encoding) but uses `_` instead of `%`
* **Lenient parsing**: Invalid hex digits are copied without modification
* **Example**: `_21` → `!`, `_25` → `%`, `_26` → `&`, `_3F` → `?`

## Examples

Converting hex-encoded legend text to readable ASCII:

@@@ atlas-example { hilite=:decode }
Hex to ASCII: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=1,one_21_25_26_3F,:legend,hex,:decode
@@@

This converts the legend `one_21_25_26_3F` to `one!%&?` for better readability.

## Related Operations

* [:legend](legend.md) - Set custom legend text (often used before decoding)
* [:format](format.md) - Dynamic string formatting for legends

## See Also

* [URL Encoding](https://en.wikipedia.org/wiki/Percent-encoding) - Standard percent-encoding reference

Since: 1.5