# # Read the number of steps the HackerRank city tree will be constructed through.
# n = int(input())
# # Read distances for new edges to be added at each step.
# edge_lengths = list(map(int, input().split()))

n = 1
edge_lengths = [1]

# Initialize arrays to store number of nodes, cumulative distance-related values, and results.
nodes_count = [1]
cumulative_distances = [0]
total_distances = [0]

# Variable to store the distance between the furthest points after each step.
cross_distance = 0

# Iterate over each construction step.
for step in range(1, n + 1):
    # Current edge length for this step.
    current_edge_length = edge_lengths[step - 1]
    
    # Previous number of nodes and cumulative distance.
    previous_nodes = nodes_count[step - 1]
    previous_cumulative_distance = cumulative_distances[step - 1]
    
    # Calculate new number of nodes.
    # Each step quadruples the existing nodes and adds two new nodes.
    new_nodes_count = (nodes_count[step - 1] * 4 + 2) % 1000000007
    nodes_count.append(new_nodes_count)
    
    # Update cumulative distances using the previous distances, the number of previous nodes, and the current edge length.
    new_cumulative_distance = (
        previous_cumulative_distance * 4 + 
        (2 + 3 * previous_nodes) * cross_distance + 
        current_edge_length * (3 + 6 * previous_nodes + 2 * previous_nodes)
    ) % 1000000007
    cumulative_distances.append(new_cumulative_distance)
    
    # Calculate the total distances between all pairs of nodes.
    new_total_distance = (
        total_distances[step - 1] * 4 + 
        previous_cumulative_distance * (new_nodes_count - previous_nodes) * 4 + 
        (6 * previous_nodes * 2 + 1) * current_edge_length + 
        previous_nodes * previous_nodes * 16 * current_edge_length
    ) % 1000000007
    total_distances.append(new_total_distance)
    
    # Update cross distance for the next step.
    cross_distance = (cross_distance * 2 + 3 * current_edge_length) % 1000000007

# Output the total distance for the last step, modulo 1000000007.
print(total_distances[-1] % 1000000007)
