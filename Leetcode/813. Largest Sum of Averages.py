class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n=len(nums)
        
        @cache
        def dfs(i,left):
            # base
            if left==0:
                return sum(nums[i:])/len(nums[i:])
            
            # main
            res = float('-inf')
            for j in range(i+1,n):
                part1 = sum(nums[i:j])/len(nums[i:j])
                part2 = dfs(j, left-1)
                res = max(res, part1+ part2)
            return res
            
            
        return dfs(0,k-1)
