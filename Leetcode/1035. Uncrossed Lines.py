

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return 0
            
            if nums1[i] == nums2[j]:
                return 1 + dfs(i+1,j+1)
            else:
                return max(dfs(i+1, j), dfs(i, j+1))

        return dfs(0,0)