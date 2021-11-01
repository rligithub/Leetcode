class Solution:  # bottom up dp
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        count = 0
        # corner cases --> 计算不是最大正方形的小正方形有几个
        for i in range(m):
            if matrix[i][0] == 1:
                dp[i][0] = 1
                count += 1
        for j in range(1, n):
            if matrix[0][j] == 1:
                dp[0][j] = 1
                count += 1

        # transit formula
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                count += dp[i][j]

        return count




