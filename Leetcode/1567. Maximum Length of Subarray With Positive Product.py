class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0]>0:
            return 1
        if len(nums)==1 and nums[0] <=0:
            return 0
        if all(x>0 for x in nums): return len(nums)
        if all(x<0 for x in nums) and len(nums)%2==0: return len(nums)


        res= 0
        left, right, left_c, right_c = 1,1,0,0
        
        #print('left')
        # left
        for x in nums:
            left *= x
            if left == 0:
                left, left_c = 1,0
            else:
                left_c+=1
                if left>0:
                    res = max(res, left_c)

        #print('right')
        # right
        for x in range(len(nums)-1,-1,-1):
            x = nums[x]
            #print('right = ', right)
            #print('res = ', res)
            right*=x
            if right==0:
                right, right_c = 1,0
            else:
                right_c+=1
                if right>0:
                    res=max(res, right_c)

        return res

        # a=[1,2,3,4]
        # for x in a:
        #     print(x)
        # print('----------')
        # for i in range(len(a)-1, -1, -1):
        #     print(a[i])
        # print('----------')

