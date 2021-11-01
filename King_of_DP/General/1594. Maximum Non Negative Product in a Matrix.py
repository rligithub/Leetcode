class Solution1:  # top down dp - faster
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # 求 非负数max product
        # non negative vs negative
        mod = 10 ** 9 + 7
        memo = {}
        maxval, minval = self.dfs(grid, 0, 0, memo)
        if maxval >= 0:
            return maxval % mod
        else:
            return -1

    def dfs(self, grid, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # over the range
        if i == len(grid) or j == len(grid[0]):
            return float('-inf'), float('inf')

        # base case
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j], grid[i][j]

        # recursive --> two values
        max1, min1 = self.dfs(grid, i + 1, j, memo)
        max2, min2 = self.dfs(grid, i, j + 1, memo)

        # two values defines
        if grid[i][j] >= 0:
            maxval = max(max1, max2) * grid[i][j]
            minval = min(min1, min2) * grid[i][j]
        else:
            maxval = min(min1, min2) * grid[i][j]
            minval = max(max1, max2) * grid[i][j]

        memo[(i, j)] = maxval, minval
        return memo[(i, j)]


class Solution2:  # top down dp - slower
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        memo = {}
        maxval, minval = self.dfs(grid, 0, 0, memo)
        if maxval >= 0:
            return maxval % mod
        else:
            return -1

    def dfs(self, grid, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(grid) or j == len(grid[0]):
            return float('-inf'), float('inf')

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j], grid[i][j]

        maxval, minval = float('-inf'), float('inf')
        for dx, dy in ((1, 0), (0, 1)):
            big, small = self.dfs(grid, i + dx, j + dy, memo)
            if grid[i][j] >= 0:
                if grid[i][j] * big > maxval:
                    maxval = grid[i][j] * big
                if grid[i][j] * small < minval:
                    minval = grid[i][j] * small
            else:
                if grid[i][j] * small > maxval:
                    maxval = grid[i][j] * small
                if grid[i][j] * big < minval:
                    minval = grid[i][j] * big

        memo[(i, j)] = maxval, minval
        return memo[(i, j)]


class Solution(object):  # bottom down dp
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        memo = {}
        m = len(grid)
        n = len(grid[0])
        MOD = 10 ** 9 + 7

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0 and j == 0:
                res = grid[i][j], grid[i][j]
            else:
                candidates = []
                if i > 0:
                    top = dp(i - 1, j)
                    candidates.extend([top[0] * grid[i][j], top[1] * grid[i][j]])
                if j > 0:
                    left = dp(i, j - 1)
                    candidates.extend([left[0] * grid[i][j], left[1] * grid[i][j]])
                res = max(candidates), min(candidates)

            memo[(i, j)] = res
            return res

        res = dp(m - 1, n - 1)
        return res[0] % MOD if res[0] >= 0 else -1