# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(node):

            if not node:
                if node:
                    print('node = ', node.val)
                else:
                    print('NONE')
                print("0, 0, float('inf'), float('-inf')")
                return 0, 0, float('inf'), float('-inf')
            
            left_size, left_nodes, left_min, left_max = dfs(node.left)
            right_size, right_nodes, right_min, right_max = dfs(node.right)
            
            if left_max < node.val < right_min:
                # It is a valid BST
                current_nodes = left_nodes + right_nodes + 1
                current_min = min(left_min, node.val)
                current_max = max(right_max, node.val)
                if node:
                    print('node = ', node.val)
                else:
                    print('NONE')
                print("max(left_size, right_size, current_nodes), current_nodes, current_min, current_max = ", max(left_size, right_size, current_nodes), current_nodes, current_min, current_max)
                return max(left_size, right_size, current_nodes), current_nodes, current_min, current_max
            else:
                # It is not a valid BST
                if node:
                    print('node = ', node.val)
                else:
                    print('NONE')
                print("max(left_size, right_size), float('-inf'), float('-inf'), float('inf') = ", max(left_size, right_size), float('-inf'), float('-inf'), float('inf'))
                return max(left_size, right_size), float('-inf'), float('-inf'), float('inf')
        

        print('final, df = ', dfs(root))
        print('dfs(root)[0] = ', dfs(root)[0])
        return dfs(root)[0]

