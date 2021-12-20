class Solution1:  # TLE
    def maxPoints(self, points: List[List[int]]) -> int:

        memo = {}
        return self.dfs(points, 0, -1, memo)

    def dfs(self, points, row, col, memo):
        if (row, col) in memo:
            return memo[(row, col)]

        if row == len(points):
            return 0

        res = float('-inf')
        for i in range(len(points[0])):
            if col == -1:
                res = max(res, points[row][i] + self.dfs(points, row + 1, i, memo))
            else:
                res = max(res, points[row][i] + self.dfs(points, row + 1, i, memo) - abs(col - i))
        memo[(row, col)] = res
        return memo[(row, col)]


import functools


class Solution2:  # TLE
    def maxPoints(self, points) -> int:
        m, n = len(points), len(points[0])

        @functools.lru_cache(None)
        def dfs(row, col):
            if row == m:
                return 0
            res = 0

            for k in range(n):
                # just started, then no cost
                if col == -1:
                    res = max(res, dfs(row + 1, k) + points[row][k])
                else:
                    res = max(res, dfs(row + 1, k) + points[row][k] - abs(col - k))

            return res

        res = dfs(0, -1)
        dfs.cache_clear()
        return res


class Solution:
    def maxPoints(self, points) -> int:
        m, n = len(points), len(points[0])
        dp = [0] * n
        # initialization
        for j in range(n):
            dp[j] = points[0][j]

        for i in range(1, m):

            # from left to right, find max score that next row can get --> only take into account only elements with index [0, j]
            maxx = -float("inf")
            for j in range(0, n):
                maxx = max(maxx - 1, dp[j])
                dp[j] = maxx

            # from right to left, find max score that next row can get --> only take into account only elements with index [j, end]
            maxx = -float("inf")
            for j in range(n - 1, -1, -1):
                maxx = max(maxx - 1, dp[j])
                dp[j] = maxx

            for j in range(n):
                dp[j] = points[i][j] + dp[j]

        return max(dp)