def pylons(k, arr):
    n = len(arr)
    plants = 0
    i = 0

    while i < n:
        # Find the farthest city within the current range where a power plant can be placed
        found = False
        for j in range(min(i + k - 1, n - 1), max(i - k, -1), -1):
            if arr[j] == 1:
                plants += 1
                i = j + k
                found = True
                break
        
        if not found:
            return -1
    
    return plants

# Example usage
n, k = 6, 2
arr = [0, 1, 1, 1, 1, 0]
print(pylons(k, arr))  # Output: 2
