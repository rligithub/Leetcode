class Solution1:
    def tilingRectangle(self, n: int, m: int) -> int:
        min_steps = max(n, m)
        arr = [[False for j in range(m)] for i in range(n)]

        @lru_cache(None)
        def astar(remain):
            if remain == 0:
                return 0
            res = remain
            i = 1
            while i * i <= remain:
                res = min(res, astar(remain - i * i) + 1)
                i += 1
            return res

        def dfs(steps, i, j, remain):
            nonlocal min_steps, arr, n, m
            if steps + astar(remain) >= min_steps:
                return
            if i >= n:
                min_steps = min(min_steps, steps)
                return
            if j >= m:
                dfs(steps, i + 1, 0, remain)
                return
            if arr[i][j]:
                dfs(steps, i, j + 1, remain)
                return
            u_range = 0
            for u in range(0, min(n, m)):
                if i + u >= n or j + u >= m or arr[i][j + u]:
                    break
                u_range = u
            for x in range(i, i + u_range + 1):
                for y in range(j, j + u_range + 1):
                    arr[x][y] = True
            for u in range(u_range, -1, -1):
                dfs(steps + 1, i, j + u + 1, remain - (u + 1) ** 2)
                for x in range(i, i + u + 1):
                    arr[x][j + u] = False
                for y in range(j, j + u + 1):
                    arr[i + u][y] = False

        dfs(0, 0, 0, n * m)
        return min_steps


class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        self.best = n * m

        def dfs(nums, count):
            if count >= self.best:
                return
            if all(h == n for h in nums):
                self.best = min(self.best, count)
                return
            i = j = min(range(m), key=lambda i: nums[i])
            while j < m and nums[j] == nums[i]:
                j += 1

            for x in range(min(j - i, n - nums[i]), 0, -1):
                dfs(nums[:i] + [nums[i] + x] * x + nums[i + x:], count + 1)

        dfs([0] * m, 0)
        return self.best


