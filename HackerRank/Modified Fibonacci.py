def fibonacciModified(t1, t2, n):
    left = t1
    right = t2
    
    for _ in range(n - 2):
        left, right = right, left + right**2

    return right
