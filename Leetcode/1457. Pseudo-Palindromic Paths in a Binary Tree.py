class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = 0
        vis = set()
        
        def dfs(node):
            nonlocal res, vis
            if node.val in vis:
                vis.remove(node.val)
            else:
                vis.add(node.val)

            if node.left is None and node.right is None:
                if len(vis) <= 1:
                    res += 1
                    
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

            if node.val in vis:
                vis.remove(node.val)
            else:
                vis.add(node.val)


        dfs(root)
        return res