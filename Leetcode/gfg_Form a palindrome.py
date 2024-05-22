# input_string = 'aa'
input_string = 'gereks'

length = len(input_string)

# Create a table of size length*length. dp_table[i][j]
# will store the minimum number of insertions 
# needed to convert input_string[i:j+1] to a palindrome.
dp_table = [[0 for _ in range(length)] for _ in range(length)]

# Fill the table
for gap in range(1, length):
    start = 0
    for end in range(gap, length):
      
        if input_string[start] == input_string[end]: # part of the palindrome, no need insertion
            dp_table[start][end] = dp_table[start + 1][end - 1] # hence number of insertion of lhs equal to that of rhs
        else: # not part of the palindrome, need insertion
            dp_table[start][end] = 1 + min(dp_table[start][end - 1], dp_table[start + 1][end])
        start += 1

# Return the minimum number of insertions 
# for input_string[0..length-1]
print(dp_table[0][length - 1])

'''
[0, 1, 2, 1, 2, 3]
[0, 0, 1, 0, 1, 2]
[0, 0, 0, 1, 2, 3]
[0, 0, 0, 0, 1, 2]
[0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0]

'''