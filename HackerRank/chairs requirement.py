
def minChairs(simuations):
    total, avail = 0,0
    for i in range(len(simuations)):
        
        x = simuations[i]
        
        print(x, total, avail)
        
        if x == 'C':
            if avail:
                avail-=1
            else:
                total +=1
        elif x =='R':
            avail +=1
        elif x=='U':
            if avail:
                avail-=1
            else:
                total +=1
        else:
            avail +=1
    return total
    
    
print(minChairs('CCRUCL'))