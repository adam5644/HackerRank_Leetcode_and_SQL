class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if len(s)==0: return 0

        if s[0]=='-':
            res = '-'
            for x in s[1:]:
                if 48<=ord(x)<=57:
                    res+=x
                else:
                    break
        elif s[0]=='+':
            res = ''
            for x in s[1:]:
                if 48<=ord(x)<=57:
                    res+=x
                else:
                    break
        else: 
            res = ''
            for x in s:
                if 48<=ord(x)<=57:
                    res+=x
                else:
                    break

        print('str res = ', res)

        if len(res)==0: return 0

        if res=='-': return 0

        res = int(res)
        #print('int res = ', res)
        if res<-2**31: 
            #print('a')
            return -2**31
        if res>2**31-1: 
           # print('b')
            return 2**31-1

        #print('c')
        return res
