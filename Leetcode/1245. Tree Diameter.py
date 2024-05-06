from collections import defaultdict

class Solution:
    def treeDiameter(self, edges) -> int:
        # Step 1: Build the graph using an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Initialize variables for tracking
        visited = set()
        longest = 0

        # Step 3: Define a recursive DFS function
        def dfs(node):
            nonlocal longest
            visited.add(node)
            max1, max2 = 0, 0  # The two longest paths from the current node
            # max1 is longest path, max2 is the second longest path

            # Explore all neighbors (children)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    path_length = dfs(neighbor) + 1
                    if path_length > max1:
                        max1, max2 = path_length, max1
                    elif path_length > max2:
                        max2 = path_length

            # Update the longest path (diameter)
            longest = max(longest, max1 + max2)
            return max1

        # Start DFS from any node (0 in this case)
        dfs(0)

        # The longest path found is the tree diameter
        return longest

edges = [[0,1],[0,2]]
print(Solution().treeDiameter(edges))