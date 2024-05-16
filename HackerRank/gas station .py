
def canCompleteCircuit(gas, cost):
    total_tank, curr_tank = 0, 0
    starting_station = 0
    
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]
        
        # If one couldn't get here
        if curr_tank < 0:
            # Pick up the next station as the starting one
            starting_station = i + 1
            # Start with an empty tank
            curr_tank = 0
    
    return starting_station if total_tank >= 0 else -1

# Example usage:
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))  # Output: 3