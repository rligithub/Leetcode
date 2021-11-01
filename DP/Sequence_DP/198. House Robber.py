class Solution:  # top down dp
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.dfs(nums, 0, memo)

    def dfs(self, nums, pos, memo):
        if pos in memo:
            return memo[pos]

        # base case --> over range
        if pos > len(nums) - 1:
            return 0

            # TWO CASES : rob vs not rob
        memo[pos] = max(self.dfs(nums, pos + 2, memo) + nums[pos], self.dfs(nums, pos + 1, memo))

        return memo[pos]


