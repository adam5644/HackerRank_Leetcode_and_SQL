def unboundedKnapsack(k, arr):
    temp=[0]*(k+1)
    for x in arr:
        for y in range(x, k+1):
            temp[y]=max(temp[y], temp[y - x] + x)
    return temp[k]

print(unboundedKnapsack(12, [6,9]))