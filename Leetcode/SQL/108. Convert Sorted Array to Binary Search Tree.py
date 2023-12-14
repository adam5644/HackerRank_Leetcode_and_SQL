# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        if n == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root
        # else: len >= 3

        x = len(nums) //2
        left = nums[:x] 
        mid = nums[x] 
        right = nums[x+1:] 
        
        root = TreeNode(mid)
        root.left = self.build(root, left) 
        root.right = self.build(root, right)

        return root

    def build(self, node, nums): # nums --> len(nums) >= 1, and sorted
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])

        if n == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            return root

        # n >= 3
        x = len(nums) //2
        left = nums[:x] 
        mid = nums[x] 
        right = nums[x+1:] 
        
        root = TreeNode(mid)
        root.left = self.build(root, left) 
        root.right = self.build(root, right)

        return root