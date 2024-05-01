class Solution:

    def jump(self, nums) -> int:
        
        n = len(nums)
        farthest = 0
        steps = 0
        next_step = 0
        
        for i in range(n - 1):
            farthest = max(i + nums[i], farthest)

            if i == next_step:
                next_step = farthest
                steps += 1
        
        return steps
    
print(Solution().jump([2,3,5,10,4]))


 
 