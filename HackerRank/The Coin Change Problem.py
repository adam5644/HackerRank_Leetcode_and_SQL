def getWays(n, c):
    res = [0] * (n + 1)  

    res[0] = 1  # There is one way to make 0 with 0 coins
    for coin in c:  # Iterate over each coin
        for amount in range(coin, n + 1):  # Update the res array for all amounts from coin to n
            res[amount] += res[amount - coin]

    return res[n]