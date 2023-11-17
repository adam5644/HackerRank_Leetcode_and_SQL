import re
### split
# split --> space delimited, lower case all

#### combine
# camel case
# method, variable --> lower case first word, then upper case
# class --> upper case first word, then upper case
# combine --> method add () at back

def s_func(c):
    c = c.replace('()','')
    c = re.sub('([A-Z]+)', r' \1', c)

    c = c.split()
    res = c[0].lower()
    
    for each in c[1:]:
        res += ' '
        res += each.lower()
        
    return res

    
def c_func(b, c):
    c = c.split()
    
    if b == 'C':
        res = c[0].capitalize()
    else:
        res = c[0].lower()
        
    for each in c[1:]:
        res += each.capitalize()
        
    if b == 'M':
        res += '()'
    return res
    

try: 
    while True:
        line = input()
        a,b,c = line.split(';')
        if a == 'S':
            print(s_func(c))
        else:
            print(c_func(b, c))
except:
    pass