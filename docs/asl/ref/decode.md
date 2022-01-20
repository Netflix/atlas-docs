@@@ atlas-signature
String
TimeSeriesExpr
-->
StyleExpr
@@@

!!! Note
    It is recommended to avoid using special symbols or trying to
    encode structural information into tag values. This feature should be used
    sparingly and with great care to ensure it will not result in a combinatorial
    explosion.

Perform decoding of the legend strings. Generally data going into Atlas
is restricted to simple ascii characters that are easy to use as part of
a URI. Most commonly the clients will convert unsupported characters to
an `_`. In some case it is desirable to be able to reverse that for the
purposes of presentation.

* `none`: this is the default. It will not modify the legend string.
* `hex`: perform a hex decoding of the legend string. This is similar to
  [url encoding](https://en.wikipedia.org/wiki/Percent-encoding) except
  that the `_` character is used instead of `%` to indicate the start of
  an encoded symbol. The decoding is lenient, if the characters following
  the `_` are not valid hexadecimal digits then it will just copy those
  characters without modification.

Since: 1.5

Example:

@@@ atlas-example { hilite=:decode }
Hex to ASCII: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=1,one_21_25_26_3F,:legend,hex,:decode
@@@