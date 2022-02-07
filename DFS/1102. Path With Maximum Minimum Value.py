class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # step1: sort all values in grid
        nums = set()
        for i in range(m):
            for j in range(n):
                nums.add(grid[i][j])
        nums = sorted(list(nums))

        # step2: binary search
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            visited = set()
            if self.dfs(nums[mid], grid, m, n, 0, 0,
                        visited):  # if nums[mid] is in the path that reach to the destination --> find largest one
                left = mid + 1
            else:
                right = mid - 1
        return nums[right]

    def dfs(self, target, grid, m, n, i, j, visited):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] < target or (i, j) in visited:
            return False
        if i == m - 1 and j == n - 1:
            return True

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if self.dfs(target, grid, m, n, x, y, visited):
                return True

        return False

