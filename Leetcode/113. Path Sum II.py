# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, cumsum, chosen):
            if not node: return 
            
            if not node.left and not node.right:
                if cumsum+node.val == targetSum:
                    res.append(chosen+[node.val])
                return

            if node.left:
                dfs(node.left, cumsum+node.val, chosen+[node.val])
            if node.right:
                dfs(node.right, cumsum+node.val, chosen+[node.val])

            
        # init
        dfs(root, 0, [])
        return res