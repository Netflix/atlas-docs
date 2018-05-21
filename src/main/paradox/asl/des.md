# Double Exponential Smoothing

@@@ atlas-graph { show-expr=true }
/api/v1/graph?q=name,sps,:eq
@@@


@@@ atlas-expr
# Query to generate the input line
nf.cluster,alerttest,:eq,
name,requestsPerSecond,:eq,:and,
:sum,

# Create a copy on the stack
:dup,

# Apply a DES function to generate a prediction
:des-fast,

# Used to set a threshold. The prediction should
# be roughly equal to the line, in this case the
# threshold would be 85% of the prediction.
0.85,:mul,

# Create a boolean signal line that is 1
# for datapoints where the actual value is
# less than the prediction and 0 where it
# is greater than or equal the prediction.
# The 1 values are where the alert should
# trigger.
:lt,

# Apply presentation details.
:rot,$name,:legend,
@@@