class Solution:
    def rob(self, nums: List[int]) -> int:
        # circled house --> check nums[1:] or nums[:-1] --> find maxx
        if len(nums) == 1:
            return nums[0]

        return max(self.dfs(nums[1:], 0, {}), self.dfs(nums[:-1], 0, {}))

    def dfs(self, nums, i, memo):
        if i in memo:
            return memo[i]

        if i >= len(nums):
            return 0

        rob = self.dfs(nums, i + 2, memo) + nums[i]
        not_rob = self.dfs(nums, i + 1, memo)

        memo[i] = max(rob, not_rob)
        return memo[i]