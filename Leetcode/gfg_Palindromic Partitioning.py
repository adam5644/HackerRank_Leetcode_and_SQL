
class Solution:
    def palindromicPartition(self, s):
        n = len(s)
        
        # Create the DP tables
        min_cuts = [0] * n
        is_palindrome = [[False for _ in range(n)] for _ in range(n)]
    
        # All substrings of length 1 are palindromes
        for i in range(n):
            is_palindrome[i][i] = True
    
        # Fill the is_palindrome table
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 2:
                    is_palindrome[start][end] = (s[start] == s[end])
                else:
                    is_palindrome[start][end] = (s[start] == s[end]) and is_palindrome[start + 1][end - 1]
    
        # Fill the min_cuts table
        for end in range(n):
            if is_palindrome[0][end]:
                min_cuts[end] = 0
            else:
                min_cuts[end] = float('inf')
                for start in range(end):
                    if is_palindrome[start + 1][end] and min_cuts[start] + 1 < min_cuts[end]:
                        min_cuts[end] = min_cuts[start] + 1
    
        # Return the minimum number of cuts needed
        return min_cuts[n - 1]
