    
    pivot = -1
    for i in range(len(w) - 2, -1, -1):
        if w[i] < w[i + 1]:
            pivot = i
            break
    
    # If no pivot found, there's no larger permutation
    if pivot == -1:
        print( "no answer")
    else: 
        # Find the smallest character on right of pivot that is greater than pivot
        for i in range(len(w) - 1, pivot, -1):
            if w[i] > w[pivot]:
                # Swap characters
                w = list(w)
                w[pivot], w[i] = w[i], w[pivot]
                w = ''.join(w)
                break
        
        # Reverse the suffix after pivot
        print( w[:pivot + 1] + ''.join(sorted(w[pivot + 1:])))