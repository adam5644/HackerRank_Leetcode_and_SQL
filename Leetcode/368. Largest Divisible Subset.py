nums = [1,2,8,4,3,6,12,24]

nums.sort()  # Sort the array to ensure divisibility property
print('nums = ', nums)

dp = [[] for _ in range(len(nums))]  # Dynamic programming array to store the largest divisible subset ending at each index
print('dp')
for i in dp:
    print(i)
print()

# Initialize the dynamic programming array
dp[0] = [nums[0]] # largest divisible subset ending at index i is just [nums[0]]

for i in dp:
    print(i)
print()

# Iterate through the array and update the dynamic programming array
for i in range(1, len(nums)):
    max_subset = [] # max subset for i
    for j in range(i):
        if nums[i] % nums[j] == 0 and len(dp[j]) > len(max_subset):
            max_subset = dp[j]
    dp[i] = max_subset + [nums[i]]
    print()

# Find the maximum length subset
max_subset = []
for subset in dp:
    if len(subset) > len(max_subset):
        max_subset = subset

print(max_subset)