class Solution:
    def minHeightShelves(self, books: List[List[int]], w: int) -> int:
        n= len(books)

        @lru_cache(None)
        def dfs(layer_h, layer_w_left, i):
        # print('res, layer_h, layer_w_left, i = ', res, layer_h, layer_w_left, i)
            
            if i==n: 
                #print('res = ', res)
                return 0

            res = float('inf')
            # a --> book i in current layer
            cw, ch = books[i][0], books[i][1]
            #print('cw, ch = ', cw, ch)

            if layer_w_left>= cw:
                max_h = max(ch, layer_h)
                res = min(res,
                    max_h-layer_h + dfs(max_h, layer_w_left-cw, i+1)
                    )


            res = min(res, ch + dfs(ch, w-cw, i+1))

            return res

        return dfs(0,0,0)