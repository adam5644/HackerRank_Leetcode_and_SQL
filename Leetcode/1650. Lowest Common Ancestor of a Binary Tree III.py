class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# Create nodes
root = Node(3)
node5 = Node(5)
node1 = Node(1)
node6 = Node(6)
node2 = Node(2)
node0 = Node(0)
node8 = Node(8)
node7 = Node(7)
node4 = Node(4)

# Establish hierarchy
root.left = node5
root.right = node1
node5.parent = root
node1.parent = root

node5.left = node6
node5.right = node2
node6.parent = node5
node2.parent = node5

node1.left = node0
node1.right = node8
node0.parent = node1
node8.parent = node1

node2.left = node7
node2.right = node4
node7.parent = node2
node4.parent = node2

# Define the solution method
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1 else q
            p2 = p2.parent if p2 else p
        return p1

# Create a solution instance
solution = Solution()

# Find LCA of node5 and node4
lca = solution.lowestCommonAncestor(node5, node4)
print("LCA of nodes 5 and 4:", lca.val)
