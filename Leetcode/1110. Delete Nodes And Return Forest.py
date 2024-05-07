class Solution:

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []

        def dfs(node, is_root):
            if not node:
                return None

            is_deleted = node.val in to_delete

            if is_root and not is_deleted:
                result.append(node)

            node.left = dfs(node.left, is_deleted)
            node.right = dfs(node.right, is_deleted)

            if is_deleted:
                return None
            else:
                return node

        dfs(root, True)
        return result