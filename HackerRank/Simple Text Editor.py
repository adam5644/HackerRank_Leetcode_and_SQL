q = int(input().strip())
l = ''
last = []
for _ in range(q):
    x = input().strip().split()

    if x[0] == '1':
        #print(1)
        last.append([1,x[1]])
        l = l+x[1]
        
    elif x[0] == '2':
        #print(2)
        k = int(x[1])
        last.append([2, l[-k:]])
        l = l[:-k] # l = 10, k = 4. len(l) - k = 6. l from index 0 to indx 5 ( 6 numbers)
        
    elif x[0] == '3':
        #print(3)
        k = int(x[1])
        print(l[k-1])
        
    else: #4
        #print(4)
        #print('last = ', last)
        if last[-1][0] == 1:
            #l = l.replace(last[-1][1],'',1)
            l = l[:-len(last[-1][1])]
        else: 
            l = l + last[-1][1]
        last.pop()
    #print('l = ',l)