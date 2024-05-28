nums = [1,2,3,4,4]
dp = [0, 0, 0]
for num in nums:
    print('num = ', num)
    for val in dp.copy():
        dp[(val+num)%3] = max(dp[(val+num)%3], num+val)
        
    print('dp = ', dp)
        
print('final dp = ', dp)
print(dp[0])