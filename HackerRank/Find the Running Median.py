import heapq

def runningMedian(a):
    res = []
    left, right = [], []

    for x in a:
        if not left or x < -left[0]:
            heapq.heappush(left, -x)
        else:
            heapq.heappush(right, x)

        # Balance the heaps
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))

        # Calculate median
        if len(left) == len(right):
            res.append((-left[0] + right[0]) / 2.0)
        else:
            res.append(float(-left[0]))

    return res
