class Solution:  # top down dp
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 有障碍物的矩阵，求有多少个路径走到终点 --> 多一个base case

        memo = {}
        return self.dfs(obstacleGrid, 0, 0, memo)

    def dfs(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(matrix), len(matrix[0])

        # stop point
        if i == m - 1 and j == n - 1 and matrix[i][j] == 0:
            return 1

        # over range
        if i > m - 1 or j > n - 1:
            return 0

            # base case
        if matrix[i][j] == 1:
            return 0

        # recursive
        memo[(i, j)] = self.dfs(matrix, i + 1, j, memo) + self.dfs(matrix, i, j + 1, memo)

        return memo[(i, j)]
