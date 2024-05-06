
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, cum:str):
            nonlocal res
            if not node: return 0
            print('before cum = ', cum)
            cum += str(node.val)
            print('after cum = ', cum)

            if not node.left and not node.right:
                res+= int(cum)
                return

            dfs(node.left, cum)
            dfs(node.right, cum)

        dfs(root, '')
        return res