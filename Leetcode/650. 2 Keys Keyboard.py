# 650. 2 Keys Keyboard

class Solution:
    def minSteps(self, n: int) -> int:
        # Initialize the operations array
        operations = [float('inf')] * (n + 1)
        operations[1] = 0  # Base case: 1 'A' needs 0 operations
        
        # Fill the operations array
        for total_A in range(2, n + 1):
            for divisor in range(1, total_A):
                if total_A % divisor == 0:  # total_A is divisible by divisor
                    operations[total_A] = min(operations[total_A], operations[divisor] + (total_A // divisor))
        
        return operations[n]