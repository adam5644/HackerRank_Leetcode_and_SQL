def countWays(n):
   
    # declaring three variables
    # and holding the ways
    # for first three stairs
    a = 1
    b = 2
    c = 4
 
    d = 0 # fourth variable
    if (n == 0 or n == 1 or n == 2):
        return n
    if (n == 3):
        return c
         
    for i in range(4,n+1): 
       
        # starting from 4 as
        d = c + b + a # already counted for 3 stairs
        a = b
        b = c
        c = d
    return d
 
 
# Driver program to test above functions
n = 4
print(countWays(n))