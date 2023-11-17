def func(a):
    res = 0 
    
    res+= max(a[0][0], a[0][3], a[3][0], a[3][3])
    res+= max(a[0][1], a[0][2], a[3][1], a[3][2])
    res+= max(a[1][0], a[1][3], a[2][0], a[2][3])
    res+= max(a[1][1], a[1][2], a[2][1], a[2][2])
            
    return res
    
    

sample_matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 83, 108]
]

print(func(sample_matrix))