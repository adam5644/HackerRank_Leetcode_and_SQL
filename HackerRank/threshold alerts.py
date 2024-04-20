from collections import deque

def maxLength(a, k):
    res = 0
    current_sum = 0
    window = deque()

    for num in a:
        window.append(num)
        current_sum += num

        while current_sum > k and window:
            popped = window.popleft()
            current_sum -= popped

        if current_sum <= k:
            res = max(res, len(window))

    return res

print(maxLength([1, 2, 3], 3))
