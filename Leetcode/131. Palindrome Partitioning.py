
class Solution:
    def partition(self, s: str):
        n = len(s)
        ans = []

        if n == 0:
            return [[]]
        
        for i in range(1, n + 1):
            if s[:i] != s[:i][::-1]: # if not palindrome, continue to next loop
                continue

            else: # if is palindrome
                cur = self.partition(s[i:])
                for j in range(len(cur)):
                    ans.append([s[:i]] + cur[j])
        return ans
    
print(Solution().partition("aab"))