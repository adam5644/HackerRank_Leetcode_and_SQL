m,r,s = map(int,input().rstrip().split())
x = list(map(int, input().rstrip().split()))

sumA = int(0.5*(r+s))
sumB = int(0.5*(r-s))

dp= [[0 for _ in range(len(x) +1)] for _ in range(sumA +1)]

# print(m,r,s,x)
# print(sumA, sumB)
# for i in dp: print(i)
# 4 5 3 [1, 1, 1, 4]
# 4 1
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]

dp[0][0] = 1

for element in x:
    for curr_sum in range(sumA, element - 1, -1):
        for count in range(1, len(x) + 1):
            if curr_sum >= element:
                dp[curr_sum][count] += dp[curr_sum - element][count - 1]
        #         print('element = ', element)
        #         print(f'dp[{curr_sum - element}][{count - 1}] = ', dp[curr_sum - element][count - 1])
        #         print(f'dp[{curr_sum}][{count}] = ', dp[curr_sum][count])
        # print()

            
# print()
# print('final dp')
# for i in dp:
#     print(i)
            
res = 0
for count in range(len(x)+1):
    res += ((dp[sumA][count] * dp[sumB][count]) %1000000007)
print(res%1000000007)