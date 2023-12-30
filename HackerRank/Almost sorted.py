def almostSorted(arr):
    # 1
    if arr == sorted(arr):
        print('yes')
        return
    
    # 2
    n = len(arr)
    arr2 = sorted(arr)
    swap = []
    for i in range(n):
        if arr[i] != arr2[i]:
            swap.append(i)
    if len(swap) == 2:
        print('yes')
        print('swap', swap[0]+1, swap[1]+1)
        return
        
    # 3
    for i in range(n):
        for j in range(i+1, n):
            if arr[i:j] == sorted(arr[i:j], reverse=True):
                print('yes')
                print('reverse',i+1,j+1)
                return  
    
    # 4
    print('no')
    return