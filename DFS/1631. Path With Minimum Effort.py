class Solution2:  # binary search + dfs
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # 一个路径耗费的最小体力是路径中相邻格子的高度差绝对值的最大值。
        # 找出每条路径中最大的diff 中最小diff
        # binary search + dfs

        m, n = len(heights), len(heights[0])
        maxx = 0
        for i in range(m):
            for j in range(n):
                maxx = max(maxx, heights[i][j])

        left, right = 0, maxx
        while left < right:
            mid = left + (right - left) // 2
            if self.dfs(heights, m, n, mid, 0, 0, heights[0][0], set()):
                right = mid
            else:
                left = mid + 1
        return left

    def dfs(self, grid, m, n, limit, i, j, prev, visited):
        if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited or abs(grid[i][j] - prev) > limit:
            return False

        if i == m - 1 and j == n - 1:
            return True

        visited.add((i, j))

        diff = 0
        for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
            x = i + dx
            y = j + dy

            if self.dfs(grid, m, n, limit, x, y, grid[i][j], visited):
                return True

        return False


class Solution1:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # binary search + dfs

        m, n = len(heights), len(heights[0])
        maxx = 0
        for i in range(m):
            for j in range(n):
                maxx = max(maxx, heights[i][j])

        left, right = 0, maxx
        while left <= right:
            mid = left + (right - left) // 2
            if self.dfs(heights, m, n, mid, 0, 0, heights[0][0], set()):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def dfs(self, grid, m, n, limit, i, j, prev, visited):
        if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited or abs(grid[i][j] - prev) > limit:
            return False

        if i == m - 1 and j == n - 1:
            return True

        visited.add((i, j))

        diff = 0
        for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
            x = i + dx
            y = j + dy

            if self.dfs(grid, m, n, limit, x, y, grid[i][j], visited):
                return True

        return False

