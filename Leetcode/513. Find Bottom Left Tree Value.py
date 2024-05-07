# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = None
        deepest = float('-inf')

        def dfs(node, depth):
            nonlocal res, deepest
            # if node:
            #     print('node.val, depth = ', node.val, depth)
            nonlocal res
            if not node: 
                return

            if not node.left and depth>deepest:
                deepest = depth
                res = node.val
            if not node.right and depth>deepest:
                deepest = depth
                res = node.val

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0) 
        #print('res, deepest = ', res, deepest)
        return res
