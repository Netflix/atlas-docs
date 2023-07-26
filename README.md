[![Release](https://github.com/Netflix/atlas-docs/actions/workflows/release.yml/badge.svg)](https://github.com/Netflix/atlas-docs/actions/workflows/release.yml)

## Atlas Docs

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

## Development

### Environment Setup

Setup a virtual environment with the appropriate Python libraries:

```bash
./setup-venv.sh
source venv/bin/activate
```

The following command will build and serve the docs locally on port 8000:

```bash
mkdocs serve
```

### MkDocs Custom Plugins

* See the [Atlas Formatting Plugin README] for details on using directives in Markdown source.
* See the [Atlas Link Checker README] for details on validating links in MkDocs site output.

[Atlas Formatting Plugin README]: ./plugins/mkdocs-atlas-formatting-plugin/README.md
[Atlas Link Checker README]: ./plugins/atlas-link-checker/README.md

### Updating Python Dependencies

```bash
./update-dependencies.sh
```

### Updating Atlas Jar

In general, this version should be kept at a release candidate, such as `1.8.0-rc.2`,
which is updated with new features regularly. Remember to delete locally cached copies
of `atlas-standalone.jar` to force a re-download of the latest release of this snapshot.

* Produce a new `atlas-standalone-$VERSION.jar` binary from the [Atlas project] on your machine.

  ```bash
  git checkout v1.7.5
  make clean
  make one-jar
  ```

* Attach the binary to a defined [Atlas release].
* Update the version specified in [config.py].

[Atlas project]: https://github.com/Netflix/atlas
[Atlas release]: https://github.com/Netflix/atlas/releases
[config.py]: ./plugins/mkdocs-atlas-formatting-plugin/mkdocs_atlas_formatting_plugin/config.py
