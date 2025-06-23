## Overview

* Consolidation is automatically applied based upon the size of the query window.
* There is a hard maximum of 1,440 datapoints per line, which is one day of data with a 1-minute step size.
* There must be at least 1 pixel per datapoint.
* The unit is preserved across consolidation.
* The consolidation function will match the aggregation function used (i.e. avg for avg/sum, max for max).

## Further Explanation

* Step size will change based on the amount of data requested.
    * For short time windows, with graphs that are the default width, you will get a 1m step size up to ~12 hours.
    * For longer time windows, such as multiple days, the step size can increase to 2m, 5m, 10m, or more.
    * The step size can change as the graph width changes - this is most often noticed on very wide monitors.
* One pixel per datapoint.
    * In addition to the hard limit on datapoints per line, the pixel width is also considered, in order to be able to
    render one pixel per data point.
    * The maximum number of datapoints for a line is the smaller of 1,440 and number of pixels that can be visualized.
    * This can be demonstrated by viewing a metric for the last day:
        * If you maximize the graph canvas, the Step size switches to 1m.
        * If you minimize the graph canvas, the Step size switches to 5m.
* Unit is preserved.
    * The y-axis unit is preserved for any step size changes.
* Consolidation function matches aggregation function.
    * Let’s say you are looking at a graph of Stream Starts per Second (SPS), which is reported by thousands of instances.
    * This is typically done with a sum aggregation, because you want to see the total value across the fleet.
    * If you look at this data across a three hour window with a default canvas size, then it will be a 1-minute step size,
    and no consolidation is applied.
    * If you expand the time range to 24 hours, then the amount of data selected is now large enough that it must be
    combined, in order to graph it.
    * The step size changes to 5-minute, and a consolidation function is applied to combine multiple minutes of data
    into a single point on the graph.
    * Since the aggregation is a sum in this case, the consolidation is an average. This means that each point on the graph
    is now the average value of the five minutes of data from the previous graph across the same time range.
    * If you had used a max aggregation, then a max consolidation would be applied. The consolidation function is automatically
    chosen on your behalf, to provide the most correct value on the graph.
    * As long as your graph lines are continuous, you should not notice any significant changes due to the application of the
    consolidation function.
    * If your graph lines are sparsely populated, with many zero or NaN values, then you will see significant changes due to
    consolidation, because zero or low values will pull down an average.
