class Solution:  # top down dp
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 背包问题 --> 加不加负号的问题

        memo = {}
        return self.dfs(nums, target, 0, memo)

    def dfs(self, nums, target, pos, memo):
        if (target, pos) in memo:
            return memo[(target, pos)]

        # solution is completed
        if target == 0 and pos == len(nums):
            return 1

        # 加不加 负号
        add, not_add = 0, 0
        # 如果pos还没到终点的话，继续操作 -- > 因为有正负号，所以不能根据 剩余的target来判断是否进行下去
        if pos < len(nums):
            add = self.dfs(nums, target + nums[pos], pos + 1, memo)

            not_add = self.dfs(nums, target - nums[pos], pos + 1, memo)

        memo[(target, pos)] = add + not_add

        return memo[(target, pos)]