def find_number_of_graphs(edges):
    from collections import defaultdict, deque

    # Build the graph
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        if v not in graph:
            graph[v] = set()  # Ensure isolated nodes are included in the graph

    visited = set()
    num_components = 0

    # Helper function to perform DFS
    def dfs(node):
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)  

    # Find all connected components
    for node in graph:
        if node not in visited:
            visited.add(node)
            dfs(node)
            num_components += 1  # Increment for each new component found

    return num_components

# Example usage
edges = [[2,1], [1,3]]
print(find_number_of_graphs(edges))  # Output should be 2 if no path connects component [1, 2, 3] with [4, 5]
