# 99. Recover Binary Search Tree
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first, second = None, None
        prev = None
        
        def dfs(node):
            nonlocal first, second, prev
            if not node:
                return
            dfs(node.left)
            
            if prev and not first: # step 2: first
                if node.val <= prev.val:
                    first = prev
            
            if first: # step 3: second
                if node.val <= first.val:
                    second = node

            prev = node # step 1: prev
            dfs(node.right)

        dfs(root)
        first.val, second.val = second.val, first.val
