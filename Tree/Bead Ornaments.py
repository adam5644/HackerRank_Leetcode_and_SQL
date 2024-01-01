def beadOrnaments(b):
    MOD = 10**9 + 7
    sumColor = sum(b)
    intercolor = 1
    for color in b:
        intercolor *= pow(color, color - 1, MOD)
    intercolor *= pow(sumColor, len(b) - 2, MOD)
    return intercolor % MOD