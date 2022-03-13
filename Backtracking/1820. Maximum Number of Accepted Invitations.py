class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        matched = [-1] * n

        count = 0
        for boy in range(m):
            visited = set()
            if self.dfs(grid, boy, visited, matched):
                count += 1
        return count

    def dfs(self, grid, b, visited, matched):

        for g in range(len(grid[0])):
            if grid[b][g] == 0 or g in visited:
                continue

            visited.add(g)

            if matched[g] < 0 or self.dfs(grid, matched[g], visited, matched):
                matched[g] = b
                return True
        return False
