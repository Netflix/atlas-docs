# Gauge Poller

Helper for polling gauges in a background thread. A shared executor is used with a single
thread. If registered gauge methods are cheap as they should be, then this should be plenty
of capacity to process everything regularly. If not, then this will help limit the damage to
a single core and avoid causing problems for the application.
