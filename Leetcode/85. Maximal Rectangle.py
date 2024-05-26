matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

n = len(matrix[0])
height = [0] * n

for row in matrix:
    for i in range(n):
        if row[i]=='1':
            height[i] = 1+height[i]
        else:
            height[i]=0
            
    