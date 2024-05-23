from collections import defaultdict

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        #print('nums = ', nums)
        n=len(nums)
        vis=set()
        dd = defaultdict(list)

        for a in range(n):
            for b in range(a+1,n):
                if a!=b and (a,b) not in vis:
                    vis.add((a,b))
                    dd[nums[a]+nums[b]].append([a,b]) # dd[sum] = [index, index]

        res=set()

        #print('dd = ', dd)

        keyy = list(dd.keys())

        for s1 in keyy:
            if dd[target-s1]:
                for a,b in dd[s1]: # index, index
                    for c,d in dd[target-s1]: # index, index
                        #print('nums[a],nums[b],nums[c],nums[d] = ', nums[a],nums[b],nums[c],nums[d])
                        #print('a,b,c,d = ', a,b,c,d)
                        if len(set([a,b,c,d])) == 4: # compare 4 indexes
                            temp=[nums[a],nums[b],nums[c],nums[d]]
                            temp.sort()
                            res.add(tuple(temp))
                            #print('include in res')
                        # else:
                        #     print('not included')
                        # print()

        return res