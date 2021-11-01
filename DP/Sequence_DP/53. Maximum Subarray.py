class Solution:  # wrong
    def maxSubArray(self, nums: List[int]) -> int:
        # 求最大sum 连续子序列 --> return max sum
        memo = {}
        self.dfs(nums, 0, memo)
        return max(memo.values())

    def dfs(self, nums, pos, memo):
        if pos in memo:
            return memo[pos]

        # base case
        if pos > len(nums) - 1:
            return 0

        res = max(nums[pos], nums[pos] + self.dfs(nums, pos + 1, memo))
        memo[pos] = res
        return memo[pos]


class Solution1:  # bottom up dp
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

            # dp[i] --> max sum in current index i

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)
