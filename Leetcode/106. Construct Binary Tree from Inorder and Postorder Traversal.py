# 106. Construct Binary Tree from Inorder and Postorder Traversal
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        
        idx = inorder.index(postorder.pop())
        root = TreeNode(inorder[idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        
        return root