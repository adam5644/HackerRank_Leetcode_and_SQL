from collections import defaultdict

n = int(input())
d=defaultdict(list)
for _ in range(n//2):
    temp = input().strip().split()
    i= int(temp[0])
    d[i].append('-')
    
for _ in range(n//2):
    temp = input().strip().split()
    i,x = int(temp[0]), temp[1]
    d[i].append(x)
    
kk = list(d.keys())
kk.sort()
 
for k in kk:
    for x in d[k]:
        print(x,end=' ')
 