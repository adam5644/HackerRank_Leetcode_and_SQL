def maxSubarray(arr):
    # Maximum subarray sum using Kadane's Algorithm
    max_ending_here = max_so_far = arr[0]
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    # Maximum subsequence sum
    # If all elements are negative, return the maximum element; otherwise, sum all positive elements.
    if all(x < 0 for x in arr):
        max_subseq = max(arr)
    else:
        max_subseq = sum(x for x in arr if x > 0)
    
    return [max_so_far, max_subseq]