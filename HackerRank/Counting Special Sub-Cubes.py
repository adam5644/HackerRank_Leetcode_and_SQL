def max2d(arr,st,n,k):
    m=n-k+2
    m2=m**2
    act_indices=[arr[st+0], arr[st+1],
                arr[st+m], arr[st+m+1],
                arr[st+m2], arr[st+m2+1],
                arr[st+m2+m], arr[st+m2+m+1]]
    #print('act_indices = ', act_indices)
    return max(act_indices)

def shrink_cube(arr, k, n):
    next_cube = []
    m = n - k + 2
    m2 = m * m
    for i in range(m - 1):
        start = m2 * i
        for j in range(m - 1):
            for z in range(m - 1):
                largest = max2d(arr, start, n, k)
                next_cube.append(largest)
                start += 1
            start += 1
    return next_cube

q = int(input())
for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr.count(1), end=' ')
    
    for k in range(2, n + 1):
        arr = shrink_cube(arr, k, n)
        print(arr.count(k), end=' ')
    print()
