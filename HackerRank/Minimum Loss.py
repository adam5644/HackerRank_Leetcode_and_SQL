numbers = [20,15,8,2,12]
n = len(numbers)
nums = list(numbers)
nums.sort()
minCost = 10**10

for i in range(1,n):
    if (nums[i]-nums[i-1] < minCost)  and (numbers.index(nums[i]) < numbers.index(nums[i-1])):
        minCost = nums[i]-nums[i-1]
        
print(minCost)