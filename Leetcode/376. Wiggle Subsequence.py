class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pu,pd=1,1

        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>0:
                pu = pd+1

            elif nums[i]-nums[i-1]<0:
                pd=pu+1

        return max(pu,pd)