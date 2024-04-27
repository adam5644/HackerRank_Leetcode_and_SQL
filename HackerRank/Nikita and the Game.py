from collections import Counter

def find_max_splits(min_val, max_val, prefix_count):
    """
    Recursive function to determine the maximum number of valid splits.
    min_val: minimum value in the current subarray range
    max_val: maximum value in the current subarray range
    prefix_count: Counter object that keeps track of prefix sums
    """
    # If the sum of the subarray (max_val - min_val) is odd, it can't be split evenly
    if (min_val + max_val) %2 !=0:
        return 0
    elif min_val == max_val:  # If the subarray contains a single unique value
        return prefix_count[min_val] - 1
    else:
        mid_val = (min_val + max_val) // 2
        # Check if mid_val is a possible split point (exists in prefix_count)
        if mid_val in prefix_count:
            # Recursively determine the max splits for the left and right subarrays
            return 1 + max(find_max_splits(min_val, mid_val, prefix_count),
                           find_max_splits(mid_val, max_val, prefix_count))
        else:
            return 0

def solve(array):
    """
    Computes the maximum number of times the array can be split.
    array: list of integers
    """
    if not array:
        return 0
    
    cumulative_sums = [0] * len(array)
    cumulative_sums[0] = array[0]
    # Build cumulative sum array
    for i in range(1, len(array)):
        cumulative_sums[i] = cumulative_sums[i - 1] + array[i]
    
    # Get the counter of cumulative sums to find potential split points
    cumulative_sum_counter = Counter(cumulative_sums)
    
    # The recursive function is called with the range from 0 to total sum of the array
    return find_max_splits(0, cumulative_sums[-1], cumulative_sum_counter)

# Input and processing loop
for _ in range(int(input())):
    _, array = input(), list(map(int, input().split()))
    print(solve(array))
