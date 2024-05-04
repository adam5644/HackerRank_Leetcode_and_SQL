class Solution:
    def longestStrChain(self, words) -> int:
        # edge
        if len(words)==1: return 1
        if all(len(w) == len(words[0]) for w in words): return 1
        
        # main
        words = sorted(words, key=lambda x: len(x))
        max_len = len(words[-1])
        d = defaultdict(list)
        for x in words:
            d[len(x)].append(x)

        @cache # secondary cache
        def prede(a, ab):
            for x in range(len(ab)):
                ab2 = ab[:x] + ab[x+1:]
                #print('ab2 = ', ab2)
                if a == ab2: return True
            return False

        # print(prede('a','ab'))
        # print('------------------')
        #print(prede('ab','acb'))

        global res
        res = 1
        @cache # main cache

        def next(last, count, last_len):
            print('last, count, last_len = ', last, count, last_len)
            global res
            res = max(res, count)
            
            # base
            if last_len + 1 not in d:
                return
            # main
            for ab in d[last_len+1]:
                if prede(last, ab):
                    next(ab, count+1, last_len+1)

        # main initiation
        for x in words:
            if res >=  max_len - len(x)+1:
                continue           
            next(x, 1, len(x))

        return min(16, res)