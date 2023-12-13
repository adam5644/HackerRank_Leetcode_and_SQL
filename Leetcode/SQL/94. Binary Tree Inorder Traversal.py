# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global res
        res = []
        if root is None:
            return res
        if root.left is not None:
            self.look(root.left)
        res.append(root.val)
        if root.right is not None:
            self.look(root.right)
        return res

    def look(self, root):
        global res
        if root.left is not None:
            self.look(root.left)
        res.append(root.val)
        if root.right is not None:
            self.look(root.right)
        