from typing import List
from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # x=[[1],[1],[2]]
        
        # nums=sorted(nums)
        # c=Counter(nums)
        # #print('c = ', c)

        # vis=set()
        # res=set()

        # n=len(nums)
        # for i in range(n):
        #     for j in range(n):
        #         if i!=j and (nums[i],nums[j]) not in vis:
        #             if nums[i]<nums[j]:
        #                 vis.add((nums[i],nums[j]))
        #             else:
        #                 vis.add((nums[j],nums[i]))
        #             summ=nums[i]+nums[j]
        #             need=0-summ
        #             #print('need = ', need)
        #             #print('c = ', c)
        #             if need in c:
        #                 temp=c[need]
        #                 if need==nums[i]:
        #                     temp-=1
        #                 if need==nums[j]:
        #                     temp-=1
        #                 if temp>=1:
        #                     x,y,z=sorted([nums[i],nums[j],need])
        #                     res.add((x,y,z))
        #             # if need in c:
        #             #     res+=c[need]
        #             # if need == nums[i]:
        #             #     res-=1
        #             # if need == nums[j]:
        #             #     res-=1


        # return list(list(x) for x in res)

        nums = sorted(nums)
        res = []
        # 2 pointers
        for i,a in enumerate(nums):
            if i> 0 and nums[i] == nums[i-1]: continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if a + nums[left] + nums[right] == 0:
                    res.append([a ,nums[left] , nums[right]]) # to append to res
                    # to skip duplicated num
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                elif a + nums[left] + nums[right] >0:
                    right -=1
                else:
                    left+=1
        # res = set(tuple(x) for x in res)
        # res = list(list(x) for x in res)
        return res