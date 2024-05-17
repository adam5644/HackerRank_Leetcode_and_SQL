class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # Initialize a list to store the length of the longest ideal subsequence ending at each letter
        l = [0] * 26
        
        # Iterate over each character in the string
        for c in s:
            i = ord(c) - 97  # Convert character to its corresponding index (0 for 'a', 1 for 'b', ..., 25 for 'z')
            
            # Calculate the range of indices to consider for the max function
            start = max(0, i - k)
            end = min(25, i + k) + 1
            
            # Update the length of the longest ideal subsequence ending at the current character
            l[i] = max(l[start:end]) + 1
        
        # Return the maximum value from the list, which represents the length of the longest ideal subsequence
        return max(l)