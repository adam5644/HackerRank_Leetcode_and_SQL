from bisect import bisect_left

S = 'abcdapzfqh'
n = len(S)

# n >=1
char_values = [ord(c) - ord('a') + 1 for c in S]
smallest_end_elements = [0] * (n + 1)
current_lis_length = 1  # Always points to the empty slot in smallest_end_elements

# Set the first value of smallest_end_elements to the first character value
smallest_end_elements[0] = char_values[0]

# Iterate through each character value starting from the second one
for i in range(1, n):
    curr_alpha = char_values[i]
    
    if curr_alpha> smallest_end_elements[current_lis_length - 1]: # next smallest_end_element will be bigger than prev ones
        # curr_alpha extends the largest increasing subsequence
        smallest_end_elements[current_lis_length] = curr_alpha
        current_lis_length += 1
    else:
        # curr_alpha will replace an element in the smallest_end_elements array
        # Find the index to replace using binary search
        replace_index = bisect_left(smallest_end_elements, curr_alpha, 0, current_lis_length - 1)
        smallest_end_elements[replace_index] = curr_alpha

print(current_lis_length)
