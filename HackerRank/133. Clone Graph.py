# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNew={}

        def dfs(node):
            if node in oldNew:
                return oldNew[node]
            copy = Node(node.val)
            oldNew[node]=copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy


        return dfs(node) if node else None
    
    
# Create the nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Setup the neighbors based on the adjacency list
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
cloned_node1 = solution.cloneGraph(node1)
    
print('')

def print_graph(node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return
    visited.add(node)
    neighbors = [n.val for n in node.neighbors]
    print(f'Node {node.val}: Neighbors -> {neighbors}')
    for neighbor in node.neighbors:
        print_graph(neighbor, visited)

print("Original Graph:")
print_graph(node1)

print("\nCloned Graph:")
print_graph(cloned_node1)
