class Solution:  # TLE
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        memo = {}
        return self.dfs(nums, 0, len(nums) - 1, memo)

    def dfs(self, nums, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i + 1 == j:
            return 0

        res = float('-inf')
        # i + 1 <= k <= j -1
        for k in range(i + 1, j):
            left = self.dfs(nums, i, k, memo)
            right = self.dfs(nums, k, j, memo)

            res = max(res, left + nums[i] * nums[k] * nums[j] + right)

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution1:  # bottom up dp
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]

        n = len(nums)

        # dp[i][j] --> max value we get from bursting balloons from index i to index j
        dp = [[0] * n for _ in range(n)]

        # 3 <= length <= n
        for length in range(3, n + 1):
            for i in range(n - (length - 1)):
                j = i + length - 1

                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

        return dp[0][-1]