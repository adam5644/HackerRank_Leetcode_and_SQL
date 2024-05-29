class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n=len(arr)

        # prefix sum
        pre_sum = {}
        pre_sum[0]= -1 # presum of 0, index -1
        pre = 0
        for i,x in enumerate(arr):
            pre+=x
            pre_sum[pre]=i

        print('pre_sum = ', pre_sum)

        # ans
        ans=float('inf')
        pre = 0
        min_left_len = float('inf')

        for i in range(n):
            pre+=arr[i]
            if pre-target in pre_sum:
                min_left_len = min(min_left_len, i-pre_sum[pre-target])
            if pre+target in pre_sum and min_left_len!=float('inf'):
                ans = min(ans, min_left_len + pre_sum[pre+target] - i)



        return ans if ans!=float('inf') else -1