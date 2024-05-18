

# Python implementation of the approach
 
import sys 
 
# Function to return the maximum required value
def knapSack(W, wt, val, n):
 
    # maxratio will store the maximum value to weight
    # ratio we can have for any item and maxindex
    # will store the index of that element
    maxratio = -sys.maxsize-1;
    maxindex = 0;
 
    # Find the maximum ratio
    for i in range(n):
        if ((val[i] / wt[i]) > maxratio):
            maxratio = (val[i] / wt[i]);
            maxindex = i;
 
 
    # The item with the maximum value to
    # weight ratio will be put into
    # the knapsack repeatedly until full
    return (W * maxratio);
 
 
# Driver code
 
val = [ 14, 27, 44, 19 ];
wt = [ 6, 7, 9, 8 ];
n = len(val);
W = 50;
 
print(knapSack(W, wt, val, n));
 
# This code is contributed by Rajput-Ji