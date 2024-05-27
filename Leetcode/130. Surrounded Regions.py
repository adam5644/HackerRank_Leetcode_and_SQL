matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

n = len(matrix[0])
heights = [0] * (n + 1)
max_area = 0

for row in matrix:
    for i in range(n):
        heights[i] = heights[i] + 1 if row[i] == "1" else 0
    print('heights = ', heights)
    
    stack = [-1] # last stack is 0
    for i in range(n + 1):
        print('i = ', i )
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        stack.append(i)
        print('stack = ', stack)
        
    print('max_area = ', max_area)
    print()
    
print(max_area)