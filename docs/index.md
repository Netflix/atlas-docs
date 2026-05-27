# Atlas

<img src="images/atlas_logo.png" width="230" height="230" align="left"></img>

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

For details and background on the project please read through the [overview](./overview.md) page.
From there, the [Stack Language](./asl/tutorial.md) tutorial is a good next step for learning how
to query and graph Atlas data, and the [Spectator](./spectator/index.md) section covers
instrumenting your own code.
