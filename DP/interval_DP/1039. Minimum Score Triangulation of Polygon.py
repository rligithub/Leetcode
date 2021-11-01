class Solution1:  # top down dp
    def minScoreTriangulation(self, values: List[int]) -> int:
        # 跟打气球一样 --> 分割成k个三角形，最少得分多少

        memo = {}
        return self.dfs(values, 0, len(values) - 1, memo)

    def dfs(self, values, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i + 1 == j:
            return 0

        res = float('inf')
        for k in range(i + 1, j):
            res = min(res,
                      self.dfs(values, i, k, memo) + self.dfs(values, k, j, memo) + values[i] * values[k] * values[j])

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution:  # bottom up dp
    def minScoreTriangulation(self, values: List[int]) -> int:

        n = len(values)
        dp = [[float('inf')] * n for _ in range(n)]

        # length == 2 两个点组成不了三角形
        for i in range(n - 1):
            dp[i][i + 1] = 0

        # length >= 3
        for length in range(3, n + 1):
            for i in range(n - (length - 1)):
                j = i + length - 1
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])

        return dp[0][-1]




