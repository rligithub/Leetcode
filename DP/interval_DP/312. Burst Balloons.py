class Solution1:  # top down dp  - TLE
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        return self.dfs(nums, 0, len(nums) - 1, memo)

    def dfs(self, nums, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i + 1 == j:
            return 0

        res = 0
        # i + 1 <= k <= j - 1

        for k in range(i + 1, j):
            res = max(res, self.dfs(nums, i, k, memo) + self.dfs(nums, k, j, memo) + nums[i] * nums[k] * nums[j])

        memo[(i, j)] = res
        return res


class Solution2:  # top down dp
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def dfs(i, j):
            if i + 1 == j:
                return 0

            res = 0
            # i + 1 <= k <= j - 1

            for k in range(i + 1, j):
                left = dfs(i, k)
                right = dfs(k, j)
                mid = nums[i] * nums[k] * nums[j]
                res = max(res, left + right + mid)

            return res

        res = dfs(0, len(nums) - 1)
        dfs.cache_clear()
        return res


class Solution:  # bottom up dp
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
