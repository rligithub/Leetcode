class Solution:
    def rob(self, nums: List[int]) -> int:

        # n == 1
        if len(nums) == 1:
            return nums[0]

        # n >= 2
        memo1, memo2 = {}, {}
        return max(self.dfs(nums[1:], 0, memo1), self.dfs(nums[:-1], 0, memo2))

    def dfs(self, nums, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos > len(nums) - 1:
            return 0

            # rob vs not_rob
        rob = self.dfs(nums, pos + 2, memo) + nums[pos]
        not_rob = self.dfs(nums, pos + 1, memo)

        memo[pos] = max(rob, not_rob)
        return memo[pos]

