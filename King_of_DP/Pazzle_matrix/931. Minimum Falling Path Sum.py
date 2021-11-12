class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # 从第一行任意位置出发，向下，左斜，右斜，到最后一行停下，求最小sum
        memo = {}
        res = float('inf')
        for j in range(len(matrix[0])):
            res = min(res, self.dfs(matrix, 0, j, memo))
        return res

    def dfs(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # over range
        if j < 0 or j >= len(matrix[0]):
            return float('inf')

        # base case
        if i == len(matrix) - 1:
            return matrix[i][j]

        res = min(self.dfs(matrix, i + 1, j - 1, memo),
                  self.dfs(matrix, i + 1, j, memo),
                  self.dfs(matrix, i + 1, j + 1, memo)) + matrix[i][j]

        memo[(i, j)] = res
        return memo[(i, j)]