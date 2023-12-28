def legoBlocks(h, w):
    mod = 10**9+7

    # su[i] is the number of ways to build a wall of width i (solid + unsolid)
    # s[i] is the number of ways to build a solid wall of width i (no vertical breaks)
    
    ww = [0] * (w+1)
    s = [0] * (w+1)
    
    ww[0] = 1  # Base case: there's one way to build a wall of width 0
    ww[1] = 1  # One block of width 1
    if w >= 2: ww[2] = 2  # Two blocks of width 1, or one block of width 2
    if w >= 3: ww[3] = 4  # Four combinations: 111, 12, 21, 3
    if w >= 4: ww[4] = 8  # Eight combinations: 1111, 112, 121, 13, 211, 22, 31, 4

    for i in range(5, w+1):
        ww[i] = (ww[i-1] + ww[i-2] + ww[i-3] + ww[i-4]) % mod

    # Solid wall of width 1 and no vertical breaks
    s[0] = 1  # Base case: there's one way to build a solid wall of width 0
    s[1] = 1  # One block of width 1

    for i in range(2, w+1):
        total = pow(ww[i], h, mod)  # Total number of ways to build the wall of height h and width i

        # Calculate the number of bad (unsolid) configurations
        bad = 0
        for j in range(1, i):
            bad += (s[j] * pow(ww[i-j], h, mod)) % mod
            bad %= mod

        # Subtract the bad configurations from total to get the solid configurations
        s[i] = (total - bad + mod) % mod  # Add mod before taking modulo to handle negative numbers

    return s[-1]  # Return the number of ways to build a solid wall of width w