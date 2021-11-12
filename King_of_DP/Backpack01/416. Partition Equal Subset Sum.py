class Solution:  # top down dp
    def canPartition(self, nums: List[int]) -> bool:
        # 求是否能把数组分成两部分 使得subset的sum 相等
        # 是否有组成 total sum //2 的解
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        memo = {}
        return self.dfs(nums, target, 0, memo)

    def dfs(self, nums, target, pos, memo):
        if (target, pos) in memo:
            return memo[(target, pos)]

        if target == 0:
            return True

        if target < 0 or pos == len(nums):
            return False

        pick = False
        if target >= nums[pos]:
            pick = self.dfs(nums, target - nums[pos], pos + 1, memo)
        not_pick = self.dfs(nums, target, pos + 1, memo)

        memo[(target, pos)] = pick or not_pick
        return memo[(target, pos)]






