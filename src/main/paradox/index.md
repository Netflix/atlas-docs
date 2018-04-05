
@@@ index

* [Overview](overview.md)
* [Getting Started](getting-started.md)
* [Concepts](concepts.md)
* [Presentations](presentations.md)
* [Stack Language](asl/index.md)
* [Reference](asl-reference/index.md)
* [Spectator](spectator/index.md)
* [Spectator Extenstions](spectator-ext/index.md)
* [Spectator Registries](spectator-reg/index.md)

@@@

@@@ warning
This site is still a work in progress @github[#1](Netflix/atlas-docs#1). Until migration is
complete, refer to:

- [Atlas Documentation](https://github.com/Netflix/atlas/wiki)
- [Spectator Documentation](https://github.com/Netflix/spectator-py)
@@@

# Atlas

<img src="https://github.com/Netflix/atlas/wiki/images/atlas_logo.png" width="230" height="230" align="left"></img>

Atlas was developed by Netflix to manage dimensional time series data for near real-time
operational insight. Atlas features in-memory data storage, allowing it to gather and report
very large numbers of metrics, very quickly.

Atlas captures operational intelligence. Whereas business intelligence is data gathered for
analyzing trends over time, operational intelligence provides a picture of what is currently
happening within a system.

Atlas was built because the existing systems Netflix was using for operational intelligence were
not able to cope with the increase in metrics we were seeing as we expanded our operations in the
cloud. In 2011, we were monitoring 2 million metrics related to our streaming systems. By 2014, we
were at 1.2 billion metrics and the numbers continue to rise. Atlas is designed to handle this
large quantity of data and can scale with the hardware we use to analyze and store it.

For details and background on the project please read through the [[overview]] page.

Check out the [[getting started]] page for an introduction to using Atlas in the cloud
environment. Once you've explored the example, check out the stack language references to see
the various types of information you can access.

