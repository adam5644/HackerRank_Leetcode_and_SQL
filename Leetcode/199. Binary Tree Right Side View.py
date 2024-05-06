# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(node, depth):
            if node:
                print('node, depth = ', node.val, depth)
            if not node:
                return
            
            if depth == len(res):
                res.append(node.val)

            helper(node.right, depth + 1)
            helper(node.left, depth + 1)
        
        helper(root, 0)
        return res