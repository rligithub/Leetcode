class Solution1:  # bottom up dp
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 求最大正方形的边长 -->min（左上角，左边，上面） + 1
        # 记录一个global值

        m, n = len(matrix), len(matrix[0])

        # dp[i][j] --> max square side length from point [0][0] to point[i][j]
        dp = [[0] * n for _ in range(m)]

        res = 0
        # transition formula
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if i > 0 and j > 0 and dp[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                res = max(res, dp[i][j])

        return res * res


class Solution:  # top down dp
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = {}
        m, n = len(matrix), len(matrix[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    res = max(res, self.dfs(matrix, i, j, memo))
        return res * res

    def dfs(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i < 0 or i > len(matrix) - 1 or j < 0 or j > len(matrix[0]) - 1:
            return 0

        if matrix[i][j] == '1':
            memo[(i, j)] = min(self.dfs(matrix, i + 1, j, memo), self.dfs(matrix, i + 1, j + 1, memo),
                               self.dfs(matrix, i, j + 1, memo)) + 1

            return memo[(i, j)]
        return 0





