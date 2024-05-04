class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        memo = {}

        def backtrack(k, bucket, nums, start, used, target):
            # 基本 case
            if k == 0:
                # 所有桶都被装满了，且 nums 全部用完
                return True
            if bucket == target:
                res = backtrack(k - 1, 0, nums, 0, used, target)
                # 缓存结果
                memo[used] = res
                return res
            if used in memo:
                # 避免冗余计算
                return memo[used]
            
            for i in range(start, len(nums)):
                if ((used >> i) & 1) == 1:
                    # nums[i] 已经被装入别的桶中
                    continue
                if nums[i] + bucket > target:
                    continue
                used |= 1 << i
                bucket += nums[i]
                if backtrack(k, bucket, nums, i + 1, used, target):
                    return True
                used ^= 1 << i
                bucket -= nums[i]
            
            return False
        
        # 确保 k 不大于 nums 的长度
        if k > len(nums):
            return False
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False       
        used = 0 # 使用位图技巧
        target = sum_nums // k # 每个桶的目标和
        # k 号桶初始什么都没装，从 nums[0] 开始做选择
        return backtrack(k, 0, nums, 0, used, target)
    #     nums.sort(reverse=True)
    #     # 排除一些基本情况
    #     if k > len(nums):
    #         return False
    #     # 将所有数的和求出来
    #     _sum = sum(nums)
    #     # 如果所有数的和不能被 k 整除，就不用继续了
    #     if _sum % k != 0:
    #         return False
    #     # 所有分出来的桶需要装 target 个数字
    #     target = _sum // k
    #     # k 个桶
    #     bucket = [0] * k
    #     # 递归穷举

    #     return self.backtrack(nums, 0, bucket, target)

    # def backtrack(self, nums, index, bucket, target):
    #     # 所有数都填完了，每个桶里的数字和都是 target
    #     if index == len(nums):
    #         for i in range(len(bucket)):
    #             if bucket[i] != target:
    #                 return False
    #         return True
        
    #     # 每个桶都尝试一下
    #     for i in range(len(bucket)):
    #         # 如果加进去这个数，这个桶的数字和就超过了 target，那就不能加了
    #         if bucket[i] + nums[index] > target:
    #             continue
    #         # 加进去
    #         bucket[i] += nums[index]
    #         # 如果这个加法是可行方案，就继续递归下去
    #         if self.backtrack(nums, index + 1, bucket, target):
    #             return True
    #         # 加完又要撤消加法，恢复现场，继续尝试别的加法
    #         bucket[i] -= nums[index]
    #     # 无解，返回 false
    #     return False