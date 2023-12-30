def pairs(k, arr):
    c = 0
    arr.sort()  # Sort the list in place
    i = 0
    j = 1
    n = len(arr)

    while j < n:
        diff = arr[j] - arr[i]
        
        # If the difference is too small, increase j to get a bigger difference
        if diff < k:
            j += 1
        # If the difference is too big, increase i to get a smaller difference
        elif diff > k:
            i += 1
        else:  # The difference is equal to k
            c += 1
            j += 1  # Move j to look for the next pair
            
            # Ensure i and j do not cross over
            if j <= i:
                j = i + 1
    return c#