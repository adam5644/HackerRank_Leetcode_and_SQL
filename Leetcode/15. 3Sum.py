# 15. 3Sum
        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if i!=j:
                    for k in range(j+1,n):
                        if k!=i:
                            #print('nums[i],nums[j],nums[k] = ', nums[i],nums[j],nums[k])
                            #print('nums[i]+nums[j]+nums[k] = ', nums[i]+nums[j]+nums[k])
                            #print('if i and j and k = ', i and j and k)
                            if nums[i]+nums[j]+nums[k]==0:
                                temp = sorted([nums[i],nums[j],nums[k]])
                                res.add(tuple(temp))
                                #print('added')
                            #else: print('not added')
        return list(res)
        # 308 