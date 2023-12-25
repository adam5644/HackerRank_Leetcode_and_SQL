def stockmax(prices):
    res = 0
    max_so_far = 0

    for i in range(len(prices) - 1, -1, -1):  # Traverse from right to left
        if prices[i] > max_so_far:
            max_so_far = prices[i]  # Update max_so_far if current price is greater
        else:
            res += max_so_far - prices[i]  # Calculate profit

    return res

# Rest of the code remains unchanged
