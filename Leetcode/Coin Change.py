def count(coins, N, sum):
    # Creating a table with dimensions (sum+1) x (N)
    table = [[0 for x in range(N)] for x in range(sum+1)]

    # Initializing the first column of the table with 1's
    for i in range(N):
        table[0][i] = 1
        
    for x in table:
        print(x)
    print()

    # Filling up the table with number of combinations
    for i in range(1, sum+1):
        for j in range(N):
            
            # Checking if using the current coin is possible
            if i-coins[j] >= 0:
                x = table[i - coins[j]][j]
            else:
                x = 0
                
            # Checking if not using the current coin is possible
            if j >= 1:
                y = table[i][j-1]
            else:
                y = 0
            
            # Adding the number of combinations to the table
            table[i][j] = x + y
            
    for x in table:
        print(x)

    # Returning the number of combinations for the given sum and coins
    return table[sum][N-1]

sum=4
N=3
coins=[1,2,3]
print(count(coins, N, sum))