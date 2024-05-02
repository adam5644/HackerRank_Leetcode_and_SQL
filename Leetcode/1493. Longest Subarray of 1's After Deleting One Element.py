
class Solution:
    def longestSubarray(self, nums) -> int:
        if len(nums)==1:
            return 0
        
        n = len(nums)
        dp = [0]*n 
        dp[0] = nums[0]
        each = []

        consecutive_0 = False

        for i in range(1,n):

            if nums[i] == 0:
                if not consecutive_0:
                    each.append(dp[i-1])
                if consecutive_0:
                    each.append(0)
            else:   
                consecutive_0 = False
                dp[i] = dp[i-1] + nums[i]

        each.append(dp[-1])

        print('dp = ', dp)
        print('each = ', each)

        print([nums[i] + nums[i-1] for i in range(1,len(each))])

        if len(each) == 0:
            return 0
        elif len(each) == 1 and 0 not in nums:
            return each[0]-1
        elif len(each) == 1 and 0 in nums:
            return each[0]
        else:
            return max(each[i] + each[i-1] for i in range(1,len(each)))

