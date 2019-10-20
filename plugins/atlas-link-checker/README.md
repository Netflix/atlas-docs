## Introduction

Check HTML links for correctness in the MkDocs build output for Atlas Docs.

```bash
./setup-venv.sh
source venv/bin/activate
mkdocs build
atlas-link-checker
```

The following categories are highlighted in the report output:

* OLD SITE LINKS. Links which point to the previous documentation site.
* BARE LINKS. Links that lack an http:// or https:// prefix.
* BAD LINKS. Links which do not return 200 OK.

Example output:

```
INFO    -  ==== Overview - Atlas Docs: site/spectator/lang/java/registry/overview/index.html ====
WARNING -  BARE LINKS:
WARNING -    <a href="../../testing">unit tests</a>
WARNING -    <a href="../metrics3">spectator-reg-metrics3</a>
WARNING -    <a href="../../testing/">testing page</a>
WARNING -    <a href="../../../../core/naming/">conventions page</a>
WARNING -    <a href="../../../../core/meters/counter/">Counters</a>
WARNING -    <a href="../../../../core/meters/timer/">Timers</a>
WARNING -    <a href="../../../../core/meters/dist-summary/">Distribution Summaries</a>
WARNING -    <a href="../../../../core/meters/gauge/">Gauges</a>
WARNING -    <a href="../../ext/log4j2/">log4j appender</a>
ERROR   -  BAD LINKS:
ERROR   -    <a href="https://static.javadoc.io/com.netflix.spectator/spectator-api/0.92.0/com/netflix/spectator/metrics3/MetricsRegistry.html">MetricsRegistry</a>
```

You can restrict the number of pages to be checked by specifying either a page title or a
filename:

```bash
atlas-link-checker --title "Overview - Atlas Docs"
atlas-link-checker --fname site/spectator/index.html
```
