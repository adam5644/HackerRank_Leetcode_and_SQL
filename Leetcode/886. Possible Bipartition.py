from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        if n <= 2:
            return True

        p_dislike = defaultdict(list)
        for a, b in dislikes:
            p_dislike[a].append(b)
            p_dislike[b].append(a)  # Since dislike is mutual

        groups = [0] * (n + 1)  # 0: not assigned, 1: group 1, -1: group 2

        def dfs(person, group): # return true if can assign "person" to "group (which can be 1 or -1"")"
            # base
            if groups[person] != 0:
                return groups[person] == group # checks whether "person" is in "group"
            # main
            groups[person] = group
            for other in p_dislike[person]:
                if not dfs(other, -group): # if the person cannot be assignede to "-group"
                    return False # return false if disliked poeple are in same group
            return True # default is true

        for i in range(1, n + 1): 
            if groups[i] == 0 and not dfs(i, 1): # assign first person as group 1 # those that are assigned group 1 or -1 are ok, they dont trigger final False
                return False

        return True

dislikes = [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]
print(Solution().possibleBipartition(10, dislikes)) # true