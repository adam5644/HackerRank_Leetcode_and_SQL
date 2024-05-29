
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        path = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
        for e in edges:
            path[e[0]][e[1]] = e[2]
            path[e[1]][e[0]] = e[2]
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if path[i][k] + path[k][j] < path[i][j]:
                        path[i][j] = path[i][k] + path[k][j]

        # Initialize the list to hold the count of reachable cities for each city
        shortest = []

        # Iterate over each row in the path matrix
        for row in path:
            # Filter the distances in the row that are within the distanceThreshold
            reachable_cities = [distance for distance in row if distance <= distanceThreshold]
            # Count the number of reachable cities and add to the shortest list
            shortest.append(len(reachable_cities))



        m = shortest[0]
        res = 0
        for i in range(len(shortest)):
            if m >= shortest[i]:
                m = shortest[i]
                res = i
        return res
 