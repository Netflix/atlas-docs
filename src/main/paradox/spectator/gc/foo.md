
# Foo

In May of 2011, Netflix was using a home-grown solution called Epic to manage
time-series data. Epic was a combination of perl CGI scripts, RRDTool logging,
and MySQL. We were tracking around 2M distinct time series and the monitoring
system was regularly failing to keep up with the volume of data. In addition
there were a number of trends in the company which presaged a drastic increase
in metric volume: