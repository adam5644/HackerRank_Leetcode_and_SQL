# 
class Solution:
    def minimumNumberOfSwaps(self, S):
        # Convert the string to a list of characters
        brackets = list(S)
        
        # Initialize counters
        open_count = 0  # Count of '[' seen so far
        close_count = 0  # Count of ']' seen so far
        swap_count = 0  # Minimum number of swaps required
        
        # Traverse the list of brackets
        for char in brackets:
            if char == ']':
                # Increment the count of ']' brackets
                close_count += 1
            else:
                # If an '[' bracket is encountered
                if close_count > open_count:
                    # We have more ']' than '[' so far, swap needed
                    swap_count += (close_count - open_count)
                # Increment the count of '[' brackets
                open_count += 1
        
        return swap_count