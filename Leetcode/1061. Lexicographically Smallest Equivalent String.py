class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        alpha_parent = {chr(x):chr(x) for x in range(97,123)}
        #print(alpha_parent)
        # print(ord('a'))
        # print(ord('z'))

        def find(x):
            if x!= alpha_parent[x]:
                alpha_parent[x] = find(alpha_parent[x])
            return alpha_parent[x]

        def union(chr1, chr2):
            p1=find(chr1)
            p2=find(chr2)
            #print('chr1, chr2 = ', chr1, chr2)
            #print('p1, p2 = ', p1, p2)
            if p1!=p2:
                if p1<p2:
                   #print('parent of ', p2, ' become ', p1)
                    alpha_parent[p2]=p1
                else:
                  #  print('parent of ', p1, ' become ', p2)
                    alpha_parent[p1]=p2
          #  print()

        for chr1, chr2 in zip(s1, s2):
            union(chr1, chr2)

        for x in range(97,123):
            #print('chr x = ', chr(x))
            find(chr(x))

        # for x in alpha_parent.items():
        #     print(x)

        # final
        res=''
        for chr1 in baseStr:
            res+=alpha_parent[chr1]
        return res