class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0

        for idx, middle in enumerate(rating):
            a = sum(left < middle for jdx, left in enumerate(rating[:idx]))
            print('left < middle for jdx, left in enumerate(rating[:idx] = ', [left < middle for jdx, left in enumerate(rating[:idx])])
            print('a = ', a)
            
            b = sum(left > middle for jdx, left in enumerate(rating[:idx]))           
            c = sum(right < middle for jdx, right in enumerate(rating[idx+1:]))
            d = sum(middle < right for jdx, right in enumerate(rating[idx+1:]))
            result += a*d + b*c

        return result