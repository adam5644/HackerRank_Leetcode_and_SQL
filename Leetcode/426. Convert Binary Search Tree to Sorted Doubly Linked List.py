# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None

        first = None
        last = None

        def helper(node):
            nonlocal first, last
            if node:
                # Traverse the left subtree
                helper(node.left)

                # Handle the current node
                if last:
                    # Link the previous node (last) with the current node
                    print('node.val = ', node.val)
                    last.right = node
                    node.left = last
                else:
                    # This condition is true for the smallest element
                    first = node
                    print('node.val = ', node.val)

                last = node  # Move last to current

                # Traverse the right subtree
                helper(node.right)

        helper(root)

        # Close the doubly linked list by linking the first and last nodes
        if first and last:
            last.right = first
            first.left = last

        return first
    
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(5)

def print_doubly_linked_list(head):
    if not head:
        return "List is empty"
    
    values = []
    current = head
    while True:
        values.append(current.val)
        current = current.right
        if current == head:
            break
    return " -> ".join(map(str, values))

solution = Solution()
head = solution.treeToDoublyList(root)
#print(print_doubly_linked_list(head))