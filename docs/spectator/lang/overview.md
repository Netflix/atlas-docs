The original Spectator library was written in [Java](java/usage.md), with the first stable version
([0.35.0]) released on Jan 18, 2016. Since then, there has been a proliferation of languages at
Netflix which seek first-class observability support.

After some thought and experimentation, we have settled on a strategy of developing minimal
Spectator implementations in many languages, which function as thin clients that send data to
Atlas. Our goal is to have partners invested in each experimental language who will provide
the necessary expertise to develop idiomatic solutions, deliver real-world feedback on library
usage, and shoulder some of the support and maintenance burden.
 
We think this is a more sustainable path over the long-term than expanding our team to support N
different languages for this singular polyglot use case.

[0.35.0]: https://github.com/Netflix/spectator/releases/tag/v0.35.0

## First-Class Support

These libraries are fully-supported by the team and see wide use across Netflix. Issues are fixed
in a timely manner and updates are published regularly.

* [Java](java/usage.md) (GA)
* [Node.js](nodejs/usage.md) (GA)

## Best-Effort Support

!!! warning
    Support for these languages is experimental and subject to change.
    
    <span style="color:red">**Do not use these libraries unless you understand and accept that
    risk.**</span>

* [C++](cpp/usage.md) (Alpha)
* [Go](go/usage.md) (Beta)
* [Python](py/usage.md) (Beta)
* [Ruby](rb/usage.md) (Alpha)
