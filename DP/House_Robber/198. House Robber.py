class Solution:  # top down do
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.dfs(nums, 0, memo)

    def dfs(self, nums, pos, memo):
        if pos in memo:
            return memo[pos]

        # base case
        if pos > len(nums) - 1:
            return 0

        rob = self.dfs(nums, pos + 2, memo) + nums[pos]
        not_rob = self.dfs(nums, pos + 1, memo)

        memo[pos] = max(rob, not_rob)
        return memo[pos]