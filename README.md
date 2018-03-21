# Atlas Docs

Experiment for moving [Atlas] documentation off of GitHub wiki and unifying with the
[Spectator] documentation. Goals:

* Avoid duplication and confusion about what information should go in Atlas wiki or
  Spectator docs.
* Provide unified search across both docs.
* Support for extensions to render Atlas graphs and format expressions. Currently this
  is done by `atlas-wiki` subproject.
* Fix some of the limitations of GitHub wiki such as page naming and ability to simply
  link to operators by substituting in the name.
* Make it easier for others to contribute to the docs.

[Atlas]: https://github.com/Netflix/atlas/
[Spectator]: https://github.com/Netflix/spectator/

# Operations

## Development

The following command will run a local webserver on port 8000:

```
sbt previewAuto
```

It does not auto-refresh the browser page on changes, but you can do this manually.

You can validate the Java examples as follows:

```
sbt compile
```

## Deployment

The following command will deploy the site to the `gh-pages` branch, where it will be available on

```
sbt ghpagesPushSite
```
