# 638. Shopping Offers
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], start_needs: List[int]) -> int:
        @cache
        def dfs(needs):
            result = sum(needs[i] * price[i] for i in range(len(needs)))
            for s in special:
                diff = tuple([n - ss for n, ss in zip(needs, s[:-1])])
                if min(diff) >= 0:
                    result = min(result, dfs(diff) + s[-1])
            return result

        return dfs(tuple(start_needs))