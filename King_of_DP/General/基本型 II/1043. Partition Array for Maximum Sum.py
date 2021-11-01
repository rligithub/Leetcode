class Solution1:  # bottom up dp
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        if not arr or k == 0:
            return 0

        n = len(arr)
        # dp[i] --> from index 0 to index i, the sum of max points arr[:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # length of substring: 1...k
            for length in range(1, k + 1):
                if i < length:
                    break
                    # 找出初始位置 i-length ， 注意padding。找出以i作为结束位置的各个长度下的最大sum --》 更新dp[i]
                dp[i] = max(dp[i], length * max(arr[i - length:i]) + dp[i - length])
        return dp[-1]


class Solution2:  # top down dp
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # 分割成subarray
        memo = {}
        return self.dfs(arr, k, 0, memo)

    def dfs(self, arr, k, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos == len(arr):
            return 0

        maxval = -1
        res = 0
        # pos作为初始位置，找各种长度的结束位置i --> 找出该长度内 最大的maxvalue
        for i in range(pos, min(pos + k, len(arr))):
            maxval = max(maxval, arr[i])
            res = max(res, maxval * (i - pos + 1) + self.dfs(arr, k, i + 1, memo))

        memo[pos] = res
        return memo[pos]


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}

        return self.dfs(arr, k, len(arr) - 1, memo)

    def dfs(self, arr, k, pos, memo):
        if pos in memo:
            return memo[pos]
        if pos < k:
            return max(arr[:pos + 1]) * (pos + 1)

        max_val = 0
        res = 0
        for i in range(k):
            max_val = max(max_val, arr[pos - i])
            res = max(res, max_val * (i + 1) + self.dfs(arr, k, pos - i - 1, memo))

        memo[pos] = res
        return memo[pos]




