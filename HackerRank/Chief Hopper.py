def chiefHopper(arr):
    nextMinEnergy = 0
    for i in range(len(arr)-1, -1, -1):
        nextMinEnergy = math.ceil((nextMinEnergy + arr[i]) / 2)
    return nextMinEnergy