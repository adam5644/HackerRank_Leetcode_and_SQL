def highestValuePalindrome(s, n, k):


    leng = len(s)
    
    # base
    if leng %2 ==0: 
        a, b = s[:leng//2], s[leng//2:]
    else:
        a,b = s[:leng//2], s[leng//2+1:]
    
    # a_idx, b_idx
    diff = 0
    leng2 = len(a)
    i, j=0, (leng2-1)
    
    a_idx, b_idx = [], []
    for _ in range(leng2):
        if a[i] != b[j]:
            a_idx.append(i)
            b_idx.append(j)
            diff += 1
        i += 1
        j -= 1
    
    # print('a = ',a)
    # print('b = ', b)
    # print('a_idx = ', a_idx)
    # print('b_idx = ', b_idx)
    
    # edge
    if diff > k:
        return '-1'
    
    # form a palindrome
    res = ''
    #print('start res = ', res)
    extra = k - diff
    #print('extra = ',extra)
    i, j=0, (leng2-1)
    for _ in range(leng2):
        if i not in a_idx:
            res += a[i]
        else:
            if a[i] > b[j]:
                if extra > 0:
                    res+='9'
                    extra -= 1
                else:
                    res+=a[i]
            else:
                if extra > 0:
                    res+='9'
                    extra -= 1
                else:
                    res+=b[i]             
        i += 1
        j -= 1
    
    #print('end res = ', res)
    
    # extra
    while extra >= 2:
        for x in res:
            if x != '9':
                res = res.replace(x,'9',1)
                break
        extra-=2
    
    # return
    if leng %2 ==1:
        if extra >= 1:
            #print('2 res = ', res)
            return res + '9' + res[::-1]
        else:
            return res + s[leng//2] + res[::-1]
            
    #print('3 res = ', res)
    return res+res[::-1]