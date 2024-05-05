# # The knows API is already defined for you.
# # return a bool, whether a knows b
# # def knows(a: int, b: int) -> bool:

# class Solution:
#     def findCelebrity(self, n: int) -> int:
#         cand = 0
#         i = 1
#         while i < n:
#             if not knows(i, cand) or knows(cand, i):
#                 cand = i
#             i += 1
#         for i in range(n):
#             if i != cand:
#                 if not knows(i, cand) or knows(cand, i):
#                     return -1
#         return cand
        

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        cand = 0
        for i in range(n): 
            if cand!=i and knows(cand, i): 
                cand = i
        # if i knows others, i is not star
        # if star is i, then first i-1 knows i, and i dont know i+1 onwards
        # to confirm i is star, test whether i knows anyone
                
        # for i in range(cand):
        #     if knows(cand, i): return -1 # dont know first i?
        #     if not knows(i, cand): return -1 # i+1 knows i?
            
        # for i in range(cand, n):
        #     if not knows(i, cand): return -1

        print('cand = ', cand)

        for i in range(n):
            if i != cand:
                if (knows(i, cand) and not knows(cand,i)):
                    continue
                else:
                    return -1
            
        return cand    
                
        