from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        @cache
        def find(left, right):
            ans = []

            # edge
            if left > right:
                ans.append(None)
                return ans
            
            # main
            for i in range(left, right + 1):
                l = find(left, i - 1)
                r = find(i + 1, right)
                for j in l:
                    for k in r:
                        root = TreeNode(i, j, k)
                        ans.append(root)
            return ans
        
        return find(1, n)
    
print(Solution().generateTrees(2))