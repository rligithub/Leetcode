class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 给一个矩阵，从[0][0] 走到尾，只能向右走或者像下走，求min path sum
        memo = {}
        return self.dfs(grid, 0, 0, memo)

    def dfs(self, grid, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(grid), len(grid[0])

        # stop point ==> 走到右下角
        if i == m - 1 and j == n - 1:
            return grid[i][j]

        # 或者 stop point ==> 走出右下角（右边/下面）
        # if (i == m and j == n-1) or (i == m-1 and j == n):
        #    return 0

        # over range
        if i > m - 1 or j > n - 1:
            return float('inf')

        # recursive
        res = min(self.dfs(grid, i + 1, j, memo), self.dfs(grid, i, j + 1, memo)) + grid[i][j]

        memo[(i, j)] = res
        return memo[(i, j)]