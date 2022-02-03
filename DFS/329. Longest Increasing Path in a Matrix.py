class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count = max(count, self.dfs(matrix, i, j, memo))
        return count

    def dfs(self, matrix, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        res = 1
        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            ii = i + di
            jj = j + dj
            if 0 <= ii < len(matrix) and 0 <= jj < len(matrix[0]) and matrix[ii][jj] > matrix[i][j]:
                res = max(res, self.dfs(matrix, ii, jj, memo) + 1)

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution:  # bottom up
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        m, n = len(matrix), len(matrix[0])

        lst = []
        for i in range(m):
            for j in range(n):
                lst.append((matrix[i][j], i, j))
        lst.sort()

        dp = [[0 for j in range(n)] for i in range(m)]
        res = 1
        for num, i, j in lst:
            dp[i][j] = 1
            for di, dj in (0, 1), (1, 0), (-1, 0), (0, -1):
                ii, jj = i + di, j + dj
                if 0 <= ii < m and 0 <= jj < n and matrix[i][j] > matrix[ii][jj]:
                    dp[i][j] = max(dp[i][j], dp[ii][jj] + 1)
                    res = max(res, dp[i][j])

        return res
