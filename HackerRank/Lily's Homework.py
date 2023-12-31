def countSwaps(arr, r):
    arr = arr.copy()
    target = sorted(arr, reverse = r)
    inds = {v:i for i,v in enumerate(target)}
    i = 0
    count = 0
    while i < len(arr) and arr != target:
        while arr[i] != target[i]:
            ind = inds[arr[i]]
            arr[i], arr[ind] = arr[ind], arr[i]
            count += 1
            print('count = ', count)
            print('arr = ', arr)
        i += 1
    return count

def lilysHomework(arr):
    return min(countSwaps(arr, False), countSwaps(arr, True))
 