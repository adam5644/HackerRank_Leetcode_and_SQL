class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # Root is always the first element in preorder traversal
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder traversal
        mid = inorder.index(root_val)
        
        # Elements to the left of `mid` are part of the left subtree
        # Elements to the right of `mid` are part of the right subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
