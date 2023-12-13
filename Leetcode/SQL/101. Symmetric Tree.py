# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        global res 
        res = True
        self.sym(root.left, root.right)
        # print('res = ', res)
        return res

    def sym(self, l_node, r_node):
        global res
        # if l_node is None:
        #     print('l = none')
        # else: 
        #     print(' l = ', l_node.val)

        # if r_node is None:
        #     print('r = none')
        # else: 
        #     print('r = ', r_node.val)

        if (l_node is None and r_node is not None) or (r_node is None and l_node is not None):
            # print('here')
            res = False
        elif (l_node is None and r_node is None):
            None
        elif (l_node.val == r_node.val):
            self.sym(l_node.left, r_node.right)
            self.sym(l_node.right, r_node.left)
        else:
            res =  False


# TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}}, right: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}}