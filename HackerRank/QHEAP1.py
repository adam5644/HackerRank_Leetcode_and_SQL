import heapq

q = int(input().strip())
heap = []
remove_set = set()  # To keep track of elements to be removed

for _ in range(q):
    query = list(map(int, input().strip().split()))
    
    if query[0] == 1:
        # Add element to the heap
        heapq.heappush(heap, query[1])
    elif query[0] == 2:
        # Mark the element for removal
        remove_set.add(query[1])
    else:
        # Remove all elements that are marked and are at the top of the heap
        while heap and heap[0] in remove_set:
            remove_set.remove(heap[0])
            heapq.heappop(heap)
        # Print the minimum element
        print(heap[0])