# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        
        global res
        res = []

        res.append([root.val])
        self.find(root.left, 1)
        self.find(root.right, 1)

        #print('res = ', res)

        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]

        #print('res = ', res)
        return res
        

    def find(self, node, lvl):
        if node is None:
            return

        global res
        if len(res) >= lvl+1: # len(res) = 3
            res[lvl].append(node.val)
        else:
            res.append([node.val])

        self.find(node.left, lvl+1)
        self.find(node.right, lvl+1)
                