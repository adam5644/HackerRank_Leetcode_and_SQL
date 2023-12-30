def arrayManipulation(n, queries):
    dp = [0] * (n + 1)
    for a, b, k in queries:
        dp[a - 1] += k
        dp[b] -= k

    max_value = 0
    current_sum = 0
    for i in dp:
        current_sum += i
        max_value = max(max_value, current_sum)
    
    return max_value
    