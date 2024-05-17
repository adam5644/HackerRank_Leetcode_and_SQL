class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)

        # edge
        if n<=2: return 0

        # main
        dp=[0]*n

        for i in range(2,n):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i]=dp[i-1]+1

        #print('dp=',dp)
        return sum(dp)