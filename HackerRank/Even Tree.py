class TreeNode:
    def __init__(self):
        self.parent = None
        self.subtree_size = 1  # Starts with 1 to count itself
    
    def link_to_parent(self, parent_node):
        """Link current node to its parent node and update the size of all ancestors."""
        self.parent = parent_node
        current_node = parent_node
        while current_node is not None: # update subtree size of all ancestors
            current_node.subtree_size += 1
            current_node = current_node.parent

if __name__ == '__main__':
    num_nodes, num_edges = map(int, input().split())  # Read number of nodes and edges
    
    # Initialize all nodes
    nodes = [TreeNode() for _ in range(num_nodes)]
    
    # Build the tree by connecting nodes to their parents
    for _ in range(num_edges):
        child_index, parent_index = map(int, input().split())
        nodes[child_index - 1].link_to_parent(nodes[parent_index - 1])
    
    # Calculate the number of edges that can be cut
    # Only count nodes that are part of an even-sized subtree and are not the root node
    num_cuts = sum(1 for node in nodes if node.subtree_size % 2 == 0 and node.parent is not None) # 1 new root = 1 new cut
    
    print(num_cuts)
