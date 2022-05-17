class Solution2:  # binary search template 3 --> find right boundary
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # smilar to swim in rising water
        # binary search max score --> check if it's valid path

        left, right = 0, min(grid[0][0], grid[-1][-1])  # must be less than grid[0][0] or grid[-1][-1]
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.isValidPath(grid, mid):
                left = mid
            else:
                right = mid

        if self.isValidPath(grid, right):
            return right
        return left

    def isValidPath(self, grid, k):
        m, n = len(grid), len(grid[0])

        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        visited.add((0, 0))

        while queue:
            i, j = queue.pop()
            if i == m - 1 and j == n - 1:
                return True

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] >= k:
                    queue.append((x, y))
                    visited.add((x, y))
        return False


class Solution:  # binary search template 1 --> find right boundary
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # smilar to swim in rising water
        # binary search max score --> check if it's valid path

        left, right = 0, min(grid[0][0], grid[-1][-1])  # must be less than grid[0][0] or grid[-1][-1]
        while left <= right:
            mid = left + (right - left) // 2
            if self.isValidPath(grid, mid):
                left = mid + 1
            else:
                right = mid - 1

        if self.isValidPath(grid, left - 1):
            return left - 1
        return left

    def isValidPath(self, grid, k):
        m, n = len(grid), len(grid[0])

        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        visited.add((0, 0))

        while queue:
            i, j = queue.pop()
            if i == m - 1 and j == n - 1:
                return True

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] >= k:
                    queue.append((x, y))
                    visited.add((x, y))
        return False



