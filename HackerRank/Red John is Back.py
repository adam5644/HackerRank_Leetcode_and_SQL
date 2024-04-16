import math

def redJohn(n): # calc brick ways
    quo = n // 4
    count = 0

    for x in range(quo, -1, -1):
        rem = n - x * 4
        count += (math.factorial(x + rem)) / (math.factorial(x) * math.factorial(rem))

    return (int(count))


def sieve(n): # calc prime
    A = [1] * (n + 1)
    A[0], A[1] = 0, 0

    print('A = ', A)
    for i in range(2, n + 1):
        print('i = ', i)
        if A[i] == 1:
            print('[0 for k in A[i * i::i]] = ', [0 for k in A[i * i::i]])
            A[i * i::i] = [0 for k in A[i * i::i]]
        print('A = ', A)

    return [k for k in range(n + 1) if A[k] == 1]



num=int(input())

for i in range(num):
    arr=[]
    n = int(input())
    print(len(sieve(redJohn(n))))