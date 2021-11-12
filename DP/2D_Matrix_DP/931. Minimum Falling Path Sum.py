class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # minimum path sum 升级版 --> 初始位置 是 第0行的任意位置， 走到 m 行 停止。

        memo = {}
        n = len(matrix[0])
        res = float('inf')
        for j in range(n):
            res = min(res, self.dfs(matrix, 0, j, memo))
        return res

    def dfs(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(matrix), len(matrix[0])
        # over range
        if j < 0 or j > n - 1:
            return float('inf')
        if i > m - 1:
            return float('inf')

        # base case
        if i == m - 1:
            return matrix[i][j]

        memo[(i, j)] = min(self.dfs(matrix, i + 1, j - 1, memo), self.dfs(matrix, i + 1, j + 1, memo),
                           self.dfs(matrix, i + 1, j, memo)) + matrix[i][j]

        return memo[(i, j)]