def countArray(n, k, x):
    MOD = 1000000007
    dpx = [0] * n
    dp0 = [0] * n
    
    if x == 1:
        dpx[0] = 1
    else:
        dp0[0] = 1
    
    for i in range(1, n):
        dpx[i] = dp0[i-1]  # Can only append '1' to sequences not ending in '1'
        dp0[i] = (dpx[i-1] * (k - 1) + dp0[i-1] * (k - 2)) % MOD  # (k-1) options if last was '1', (k-2) if last was not '1'
        
    return dpx[-1]% MOD   # The last element should be '1', so return the count of such arrays
