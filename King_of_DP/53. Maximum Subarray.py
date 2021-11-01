class Solution:  # bottom up
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)


class Solution1:  # top down
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        self.dfs(nums, 0, memo)
        return max(memo.values())

    def dfs(self, nums, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos == len(nums):
            return 0

        res = max(self.dfs(nums, pos + 1, memo) + nums[pos], nums[pos])

        memo[pos] = res
        return memo[pos]


