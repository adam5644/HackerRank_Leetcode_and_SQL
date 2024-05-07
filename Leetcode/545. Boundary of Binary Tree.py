# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # edge
        if not root.left and not root.right: return [root.val]

        #main
        res, left, right = [root.val], [], []

        # left
        def dfs_left(node, is_left):
            nonlocal left
            # base
            if not node: return
            if not node.left and not node.right: 
                left.append(node.val)
                return 
            elif is_left: left.append(node.val)
            # main
            if is_left:
                dfs_left(node.left, 1)
                if node.left:
                    dfs_left(node.right, 0)
                else:
                    dfs_left(node.right, 1)
            else:
                dfs_left(node.left, 0)
                dfs_left(node.right, 0)
        
        dfs_left(root.left, 1)
        #print('left = ', left)

        # right
        def dfs_right(node, is_right):
            nonlocal right
            # base
            if not node: return
            if not node.right and not node.left:
                right.append(node.val)
                return
            elif is_right: right.append(node.val)
            # main
            if is_right:
                dfs_right(node.right, 1)
                if node.right:
                    dfs_right(node.left, 0 )
                else:
                    dfs_right(node.left,1)
            else:
                dfs_right(node.right, 0)
                dfs_right(node.left, 0 )


        dfs_right(root.right, 1)

        # print('right = ', right)

        return res+left+right[::-1]