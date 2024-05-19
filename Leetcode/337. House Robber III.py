from typing import Optional
from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node, steal_curr):
            # base case
            if not node: return 0

            # main logic
            if steal_curr == 1:
                return node.val + dfs(node.left, 0) + dfs(node.right, 0)

            # if not stealing from the current node
            return max(
                dfs(node.left, 0) + dfs(node.right, 0), 
                dfs(node.left, 0) + dfs(node.right, 1), 
                dfs(node.left, 1) + dfs(node.right, 0), 
                dfs(node.left, 1) + dfs(node.right, 1)
            )

        # We start by considering both possibilities: stealing from the root or not
        return max(
            root.val + dfs(root.left, 0) + dfs(root.right, 0) if root else 0,
            dfs(root, 0) if root else 0
        )