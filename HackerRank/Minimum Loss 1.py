def minimumLoss(price):
    s = sorted (enumerate (price), key = lambda kv : kv[1])
    
    print('s = ', s)
    
    return min (
        (s[i+1][1] - s[i][1] for i in range (len(s) - 1) if s[i+1][0] < s[i][0])
        )