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

Setup a virtual environment with the appropriate python libraries:

```
$ ./setup-venv.sh
$ source venv/bin/activate
```

The following command will run a local webserver on port 8000:

```
$ mkdocs serve
```

