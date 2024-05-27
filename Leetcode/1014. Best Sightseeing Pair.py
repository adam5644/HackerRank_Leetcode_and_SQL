# 

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = values[0] + 0  # Initialize best to the first value plus its index (0)
        ans = 0  # Initialize the answer to zero
        
        for j in range(1, len(values)):
            # Calculate the potential score for this pair (best represents values[i] + i so far)
            ans = max(ans, best + values[j] - j)
            
            # Update best to be the maximum of its current value or values[j] + j
            best = max(best, values[j] + j)
        
        return ans
