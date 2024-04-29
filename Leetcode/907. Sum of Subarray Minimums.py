class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        arr = [float('-inf')] + arr + [float('-inf')]
        #print('arr = ', arr)
        stack = [] # monotonic increasing stack

        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                val_i = stack.pop()
                right_i = i
                left_i = stack[-1]

                #print(f'{curr_val} * ({i} - {curr_min}) * ({curr_min} - {prev_min})')
                res += arr[val_i] * (right_i - val_i) * (val_i - left_i)

            stack.append(i) # i is curr_min
            # print('stack = ', stack)
            # print('res = ', res)
            # print()

        return res%(10**9+7)

# class Solution:
#     def sumSubarrayMins(self, A: List[int]) -> int:
#         A = [-math.inf] + A + [-math.inf]
#         n = len(A)

#         st = []
#         res = 0

#         for i in range(n):
#             while st and A[st[-1]] > A[i]:
#                 mid = st.pop()
#                 left = st[-1]  # previous smaller element
#                 right = i  # next smaller element

#                 res += A[mid] * (mid - left) * (right - mid)

#             st.append(i)

#         return res % (10**9 + 7)
