arr = [1,1,2]

res = set()
prev = set()

for a in arr:
    local = set()
    local.add(a)
    
    for b in prev:
        local.add(b|a)
    prev = local # store all bitwise OR ending at index i
    
    res |= prev
    
print(len(res))