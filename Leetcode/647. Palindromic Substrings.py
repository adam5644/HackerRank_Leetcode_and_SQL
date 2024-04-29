class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        global res
        res = len(s)
        
        def calc_para(l, r):
            #print('l = ', l)
            #print('r = ', r)
            global res
            # base
            if l < 0 or r >= n:
                #print('base')
                return
            if s[l] == s[r]:
                res +=1
                calc_para(l-1, r+1)
            else:
                #print('base2')
                return       
                
        print('before single res = ', res)
        
        # single mid
        for i in range(n):
            #print('i = ', i)
            calc_para(i-1, i+1)
            
        #print('after single res = ', res)
        
        # double mid
        for i in range(n-1): # last one is (n-2, n-1)
            if s[i] == s[i+1]:
                res +=1
                calc_para(i-1, i+2)
                
        #print('after double res = ', res)
                
        return res
        