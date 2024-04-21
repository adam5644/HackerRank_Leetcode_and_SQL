from collections import defaultdict

def summingPieces(arr):
    n = len(arr)
    mod = 10 ** 9 + 7

    # contributions will store the contributions of each element for all possible segments
    contributions = [0] * (n // 2 + n % 2)
    contributions[0] = pow(2, n, mod) - 1  # First element contribution

    # Calculate the contributions for each position up to half the length of the array.
    for i in range(1, n // 2 + n % 2):
        contributions[i] = (
            contributions[i - 1] + pow(2, n - 1 - i, mod) - pow(2, i - 1, mod)
        ) % mod

    print('contributions = ', contributions)

    # We use a defaultdict to store contributions mapped by index. This isn't strictly
    # necessary but keeps alignment with your original structure.
    dp = defaultdict(list)
    print('dp = ', dp)
    # Combine contributions for both halves, the second half is a mirror of the first.
    
    dp[n] = contributions + contributions[:n // 2][::-1]
    print('contributions = ', contributions)
    print('contributions[:n // 2][::-1] = ', contributions[:n // 2][::-1])
    print('dp = ', dp)

    # Calculate the sum of all segment contributions times their corresponding array values.
    # result = sum((dp[n][i] * arr[i]) for i in range(n))
    
    result = 0
    for i in range(n):
        result += (dp[n][i] * arr[i])
        print('dp[n][i] * arr[i] = ', dp[n][i] * arr[i])
        print('result = ', result)

    return result

# Example usage
if __name__ == '__main__':
    arr = [1,3,6]
    print(summingPieces(arr))  # This would print the output for the given array.
