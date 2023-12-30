def hackerlandRadioTransmitters(x, k):
    x.sort()
    n = len(x)
    
    i = 0
    c = 0 
    while i < n:
        c+=1
        loc = x[i] + k
        while i<n and x[i] <= loc:
            i+=1
            
        loc = x[i-1] +k
        while i<n and x[i] <= loc:
            i+=1
        
    return c