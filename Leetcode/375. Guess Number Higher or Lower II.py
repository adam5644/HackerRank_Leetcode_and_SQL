 
def recurse(min_: int, max_: int) -> int:
    if min_ >= max_:
        return 0
    
    print('min_, max_ = ', min_, max_)
    for pivot in range(max_ - 1, min_ - 1, -2):
        print('pivot = ', pivot)
    print()
    
    return min(
        pivot + max(
            recurse(min_, pivot - 1), recurse(pivot + 1, max_)
            )
        for pivot in range(max_ - 1, min_ - 1, -2)
    )

print(recurse(1,3))