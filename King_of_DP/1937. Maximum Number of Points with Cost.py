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


