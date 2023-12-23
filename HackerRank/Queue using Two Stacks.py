# Enter your code here. Read input from STDIN. Print output to STDOUT

# import deque

# pop_left
# a = deque(lst)

# def funct1(lst, a):        
#     if a == 2:
#         lst = lst[1:]
#         print('type 2')
        
#     else: # 3
#         print(lst[0])
#         print('type 3')
        
#     print(lst)

# def funct2(lst, x):
#     lst.append(x)
#     print('type 1')
#     print(lst)
    


lst = []
q = int(input().strip())
for _ in range(q):
    a = list(map(int,input().strip().split())) # list of 1 int or 2 int
    if a[0] == 1:
        lst.append(a[-1])
    elif a[0] == 2:
        lst = lst[1:]
    else:
        print(lst[0])