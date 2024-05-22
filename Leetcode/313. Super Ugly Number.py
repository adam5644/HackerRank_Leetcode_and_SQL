
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = primes.copy()
        heapq.heapify(nums)
        seen = set(nums)
        
        p = 1
        for i in range(n-1):
            p = heapq.heappop(nums)
            for prime in primes:
                new_ugly = p * prime
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(nums, new_ugly)
        
        return p