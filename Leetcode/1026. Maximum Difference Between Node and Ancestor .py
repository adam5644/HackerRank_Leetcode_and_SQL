# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, min_val: int, max_val: int) -> int:
            if not node:
                return max_val - min_val
            
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            
            left_diff = dfs(node.left, min_val, max_val)
            right_diff = dfs(node.right, min_val, max_val)
            
            return max(left_diff, right_diff)
        
        return dfs(root, root.val, root.val)

# Example usage
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(13)

sol = Solution()
print(sol.maxAncestorDiff(root))  # Output should be 7
