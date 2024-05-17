class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        # Start with the base cases
        count = 10  # For n = 1 (0 to 9)
        unique_digits = 9  # For the first digit (1 to 9)
        available_digits = 9  # Remaining choices for subsequent digits
        
        for i in range(2, n + 1):
            unique_digits *= available_digits
            count += unique_digits
            available_digits -= 1
        
        return count