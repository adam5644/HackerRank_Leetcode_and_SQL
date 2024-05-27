
# 
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], fl: int, sl: int) -> int:
        res = float('-inf')
        n = len(nums)

        for i in range(n-fl+1):
            for j in range(i+fl, n-sl+1):

                temp=sum(nums[i:i+fl])+sum(nums[j:j+sl])
                if temp > res: 
                    res = temp

        if sl!=fl:
            for i in range(n-sl+1):
                for j in range(i+sl, n-fl+1):
                    temp=sum(nums[i:i+sl])+sum(nums[j:j+fl])
                    if temp > res: res = temp

        return res