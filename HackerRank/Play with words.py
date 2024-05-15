str1=input()
n=len(str1)
table=[[1 for _ in range(n)] for _ in range(n)]
 
    
# for x in table:
#     print(x)
    
for sl in range(2,n+1):
    for i in range(n-sl+1):
        j=i+sl-1
        if str1[i]==str1[j] and sl==2:
            table[i][j]=2
        elif str1[i]==str1[j]:
            table[i][j]=table[i+1][j-1]+2
        else:
            table[i][j]=max(table[i][j-1],table[i+1][j])
            
# for x in table:
#     print(x)
            
res=0
for i in range(n):
    if i+1<n:
        temp = table[0][i]*table[i+1][n-1]
        if temp > res:
            res=temp

# print()
# print(lis1)
        
print(res)
            