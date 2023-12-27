def truckTour(petrolpumps):
    # Write your code here
    n = len(petrolpumps)
    total_petrol = 0
    total_distance = 0
    start_index = 0
    surplus = 0

    for i in range(n):
        petrol, distance = petrolpumps[i]
        total_petrol += petrol
        total_distance += distance
        surplus += petrol - distance

        # If surplus is negative, reset surplus and move start index to i + 1
        if surplus < 0:
            surplus = 0
            start_index = i + 1

    return start_index

# The rest of the code can remain unchanged.
