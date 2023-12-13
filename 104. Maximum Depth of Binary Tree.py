# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global res
        res = 1
        if root is None: return 0

        if root.left is not None:
            self.look(root.left, 2)

        if root.right is not None:
            self.look(root.right, 2)

        return res

    def look(self, root, n ):
        # print('root = ', root.val)
        # print('n = ', n)
        global res
        if n > res:
            res = n 
        if root.left is not None:
            self.look(root.left, n+1)

        if root.right is not None:
            self.look(root.right, n+1)