from functools import cache
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        
        @cache
        def dfs(k):
            if k == 1:
                return [TreeNode(0)]
            
            ans = []
            for i in range(1, k, 2):
                left_trees = dfs(i)
                right_trees = dfs(k - i - 1)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans

        return dfs(n)