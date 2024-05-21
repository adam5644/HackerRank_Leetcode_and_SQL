
arr1, m, arr2, n =  [3,4,1,2,6,3], 6,[3,5,4,1,2,3], 6

dp = [0 for i in range(n)] 
# initializing an array to store the Longest Common Increasing Subsequence (LCIS) lengths for each element in arr2
print('initial, dp = ', dp)

for i in range(m):  # iterating through arr1
    current = 0  # initializing a variable to keep track of the current LCIS length
    for j in range(n):  # iterating through arr2
        if(arr1[i] == arr2[j]):  # if the current elements of arr1 and arr2 are equal
        
            dp[j] = max(dp[j], current+1)  
            # update the LCIS length for the current element in arr2 by taking the maximum of the previous LCIS
            #... length and the current LCIS length incremented by 1
            
        if(arr1[i] > arr2[j]):  # if the current element of arr1 is greater than the current element of arr2
        
            current = max(current, dp[j])  # update the current LCIS length to the maximum of the previous current 
                                            # ...length and the LCIS length for the current element in arr2
                                            
    print('dp = ', dp)
    
print('final, dp = ', dp)
print(max(dp))