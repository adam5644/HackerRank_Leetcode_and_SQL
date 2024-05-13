
m, x, dimensions = 3, [1, 1], [2, 3]
MOD = 10 ** 9 + 7
num_dimensions = len(dimensions)

# md stores the number of ways to end at each step from 0 to m for each dimension
ways_to_end_at_step = [[0 for _ in range(num_dimensions + 1)] for _ in range(m + 1)]
# ways_to_end_at_step[i][j]=x --> x ways to move in dimension j using i steps. this j is for all dimensions
#print('initial, ways_to_end_at_step = ', ways_to_end_at_step)

# Compute ways for each dimension separately
for dim in range(num_dimensions):
    max_pos = dimensions[dim]
    # M stores the number of ways to reach each position for each step count in the current dimension
    ways_in_dim = [[0 for _ in range(m + 1)] for _ in range(max_pos + 1)]
    # ways_in_dim[j][i]=x --> x ways to go to state j using i step. this j is only for this dimension
    
    # Initialize base case: 1 way to stay at each position with 0 steps
    for position in range(1, max_pos + 1):
        ways_in_dim[position][0] = 1
    
    # Compute ways to reach each position for each step count
    for step in range(1, m + 1):
        for pos in range(1, max_pos + 1):
            # Add ways from the position before and after the current position
            if pos > 1:
                ways_in_dim[pos][step] = (ways_in_dim[pos][step] + ways_in_dim[pos - 1][step - 1]) % MOD
            if pos < max_pos:
                ways_in_dim[pos][step] = (ways_in_dim[pos][step] + ways_in_dim[pos + 1][step - 1]) % MOD
    
    # Store results in ways_to_end_at_step
    for step in range(m + 1):
        #print(f'ways_in_dim[{x[dim]}][{step}] = ', ways_in_dim[x[dim]][step])
        ways_to_end_at_step[step][dim + 1] = ways_in_dim[x[dim]][step]
    #print('after, ways_to_end_at_step = ', ways_to_end_at_step)
        
# dim= 0
# initial, ways_to_end_at_step =  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# ways_in_dim[1][0] =  1
# ways_in_dim[1][1] =  1
# ways_in_dim[1][2] =  1
# ways_in_dim[1][3] =  1
# after, ways_to_end_at_step =  [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
# dim= 1
# initial, ways_to_end_at_step =  [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
# ways_in_dim[1][0] =  1
# ways_in_dim[1][1] =  1
# ways_in_dim[1][2] =  2
# ways_in_dim[1][3] =  2
# after, ways_to_end_at_step =  [[0, 1, 1], [0, 1, 1], [0, 1, 2], [0, 1, 2]]
# 12


# Compute combinations of step distributions across dimensions using Pascal's triangle for combinations
combinations = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
#print('initial, combinations = ', combinations)

for i in range(m + 1):
    combinations[i][0] = 1
    combinations[i][i] = 1
    for j in range(1, i):
        combinations[i][j] = (combinations[i - 1][j - 1] + combinations[i - 1][j]) % MOD
#print('after, combinations = ', combinations)


# Compute total ways by combining steps across all dimensions
total_ways = [[0 for _ in range(num_dimensions + 1)] for _ in range(m + 1)]
# total_ways[step][jth dimension] = x ways

print('initial, total_ways = ', total_ways)
print('initial, ways_to_end_at_step = ', ways_to_end_at_step)

for i in range(m + 1):
    total_ways[i][1] = ways_to_end_at_step[i][1] # ways_to_end_at_step[i step][dimension 1]
for dim in range(num_dimensions + 1):
    total_ways[0][dim] = 1
for dim in range(2, num_dimensions + 1):
    for step in range(1, m + 1):
        for k in range(step + 1):
            aa= combinations[step][step - k] 
            bb= (total_ways[k][dim - 1] * ways_to_end_at_step[step - k][dim]) % MOD
            ab= (aa*bb % MOD)
            total_ways[step][dim] = (total_ways[step][dim] + ab) % MOD

print('after, total_ways = ', total_ways)
print(total_ways[m][num_dimensions])