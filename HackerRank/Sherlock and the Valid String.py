s = input()

from collections import Counter

c = Counter(s)
values = c.values()
c2 = Counter(values)
 
k = list(c2.keys())
 
if len(c2.keys()) == 1:
    print('YES') 
elif len(c2.keys()) == 2:
    key1, key2 = k[0], k[1]
    if (c2[key1] == 1 and (key1 - 1 == key2 or key1 - 1 == 0)) or \
       (c2[key2] == 1 and (key2 - 1 == key1 or key2 - 1 == 0)):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
