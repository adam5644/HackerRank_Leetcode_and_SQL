# 553. Optimal Division
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums)==1:
            return str(nums[0])
        if len(nums)==2:
            return str(nums[0]) +'/'+ str(nums[1])

        res = str(nums[0]) + '/('
        for x in nums[1:-1]:
            res+=str(x) + '/'
        res+=str(nums[-1]) + ')'
        print('res = ', res)
        return res