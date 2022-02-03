class Solution1:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # binary search between 1...n to find height that can reach to bottom right
        # find min height that reach reach to bottom right
        n = len(grid)
        left, right = 0, n * n
        while left < right:
            mid = (left + right) // 2
            if self.dfs(grid, n, 0, 0, mid, set()):
                right = mid
            else:
                left = mid + 1
        return left

    def dfs(self, grid, n, i, j, limit, visited):
        if i < 0 or i >= n or j < 0 or j >= n:
            return False
        if (i, j) in visited:
            return False
        if grid[i][j] > limit:
            return False
        # Need to make sure check all false before check true
        if i == n - 1 and j == n - 1:
            return True
        visited.add((i, j))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = i + dx
            y = j + dy
            # We only need one path to get true
            if self.dfs(grid, n, x, y, limit, visited):
                return True
        return False


