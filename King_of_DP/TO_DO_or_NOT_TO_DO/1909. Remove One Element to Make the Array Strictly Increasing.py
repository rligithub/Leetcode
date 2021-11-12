class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # 如果删掉一个数 能否使得整个数组是递增的
        # 换一个思路求LIS，看看 len(nums) -  LIS <= 1
        memo = {}
        LIS = 0
        for i in range(len(nums)):
            LIS = max(LIS, self.dfs(nums, i, memo) + 1)
        print(LIS)
        return len(nums) - LIS <= 1

    def dfs(self, nums, pos, memo):
        if pos in memo:
            return memo[pos]

        # over range
        if pos == len(nums):
            return 0

        res = 0
        for i in range(pos, len(nums)):
            if nums[i] > nums[pos]:
                res = max(res, self.dfs(nums, i, memo) + 1)

        memo[pos] = res
        return memo[pos]
