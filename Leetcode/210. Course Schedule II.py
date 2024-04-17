from collections import defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        # res holds the topologically sorted order of courses
        # visited keeps track of the status of each course:
        # False if the course has been fully processed (all dependencies resolved),
        # True if the course is currently being processed (used to detect cycles),
        # None if the course hasn't been visited yet.
        res, visited = [], {}
        
        # premap is a dictionary mapping each course to a list of its prerequisites.
        premap = defaultdict(list)
        for i, j in prerequisites:
            premap[i].append(j)
        
        def dfs(i):
            if i in visited:
                # If we have visited this node, return the state:
                # True if a cycle is detected, False if already processed.
                return visited[i]
            visited[i] = True  # Mark this node as being processed
            
            # Recursively visit all the prerequisites for this course
            for j in premap[i]:
                if dfs(j):
                    # If dfs returns True, a cycle is detected
                    return True
            
            # Mark this course as fully processed
            visited[i] = False
            # Append the course to the result as all its prerequisites are processed
            res.append(i)
        
        # Try to process each course
        for i in range(numCourses):
            if dfs(i):  # If a cycle is detected during the processing of a course
                return []  # return an empty array as it's impossible to finish all courses
        
        return res  # Return the topologically sorted order of courses

print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))