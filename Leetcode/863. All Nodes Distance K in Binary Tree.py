
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parent(node, parent):
            if node is None:
                return
            node.parent = parent # add a new attribute to treenode class
            add_parent(node.left, node)
            add_parent(node.right, node)
        
        def dfs(node, parent, dist):
            # if node:
            #     print('node.val, res= ', node.val, res)

            if node is None:
                return
            if dist == k:
                res.append(node.val)
                return

            nonlocal vis
            vis.add(node.val)

            if node.parent and node.parent.val not in vis:
                dfs(node.parent, node, dist + 1)
            if node.left and node.left.val not in vis:
                dfs(node.left, node, dist + 1)
            if node.right and node.right.val not in vis:
                dfs(node.right, node, dist + 1)
 
        vis = set()
        res = []
        add_parent(root, None)
        dfs(target, None, 0)
        return res
        