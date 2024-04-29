55 jump game

nums = [2,3,1,1,4]

gas = 0
for n in nums:
    if gas < 0:
        print('false')
    elif n > gas:
        gas = n
    gas -= 1
    
print('true')