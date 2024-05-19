#Back-end complete function Template for Python 3

from sys import setrecursionlimit
setrecursionlimit(10**7)

class Solution:
    #Function to calculate nth Fibonacci number using top-down approach.
    def topDown(self, n):
        #Inner function to calculate Fibonacci number using recursion and memoization.
        def fn(n):
            if n <= 1:
                return n
            if n in dp:
                return dp[n]
            ans = (fn(n - 1) + fn(n - 2)) % M
            dp[n] = ans
            return ans
        
        dp = {} #Dictionary to store calculated Fibonacci numbers.
        M = 10**9 + 7 #Modulus value for Fibonacci calculation.
        return fn(n) #Calling inner function with input n.
    
    #Function to calculate nth Fibonacci number using bottom-up approach.
    def bottomUp(self, n):
        M = 10 ** 9 + 7 #Modulus value for Fibonacci calculation.
        dp = [0] * (1 + n) #List to store Fibonacci numbers.
        dp[0] = 0 #Fibonacci number at index 0 is 0.
        dp[1] = 1 #Fibonacci number at index 1 is 1.
        #Iterating from index 2 to n to calculate Fibonacci numbers.
        for i in range(2, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % M #Calculating Fibonacci number.
        return dp[n] #Returning Fibonacci number at index n.