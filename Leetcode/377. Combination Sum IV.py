class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(target):
            for x in nums:
                if i+x<=target:
                    dp[i+x]+=dp[i]
        return dp[target]