from collections import defaultdict, deque
from typing import Optional, List, Union

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        def DFS(curr):
            nonlocal ans

            if curr is None: return 0 # if leaf

            left = DFS(curr.left)
            right = DFS(curr.right)

            print(curr.val, left, right, ans)

            if curr.val == start: # possibility 1: max of start's left and right child
                ans = max(left, right) 
                depth = -1
            elif left >= 0 and right >= 0: # for most nodes
                depth = max(left, right ) + 1
            else:  # left <=0 or right<=0

                distance = abs(left) + abs(right)
                ans= max(ans, distance)
                depth = min(left, right) - 1

            return depth

        ans = 0
        DFS(root)
        return ans

def build_tree_from_list(values: List[Union[int, None]]) -> Optional[TreeNode]:
    if not values:
        return None

    iter_values = iter(values)
    root = TreeNode(next(iter_values))
    queue = deque([root])

    while queue:
        node = queue.popleft()
        try:
            left_val = next(iter_values)
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            right_val = next(iter_values)
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
        except StopIteration:
            break

    return root

if __name__ == "__main__":
    # values = [1, 5, 3, None, 4, 10, 6, 9, 2]
    # start = 3
    values = [1, 5, 3, None, 4, 10, 6, 9, 2, 12,8]
    start = 10
    root = build_tree_from_list(values)
    solution = Solution()
    result = solution.amountOfTime(root, start)
    print("Amount of time for binary tree to be infected:", result)
