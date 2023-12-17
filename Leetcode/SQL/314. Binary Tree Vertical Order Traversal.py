# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = collections.defaultdict(list)
        def helper(node, row, col):
            if not node:
                return
            ans[col].append((row, node.val))
            helper(node.left, row + 1, col - 1)
            helper(node.right, row + 1, col + 1)

        helper(root, 0, 0)

        print(ans)

        ans = dict(sorted(ans.items()))
        print(ans)
        res = []
        for k, v in ans.items():
            res.append([x[1] for x in sorted(v, key=lambda x:x[0])])
        
        print(res)
        return res