class Solution:  # faster
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # 两个机器人摘樱桃， 一个从[0,0] 一个从[0,-1]出发，到底就停，可以左斜，向下，右斜走，问最多能摘多少樱桃

        memo = {}
        return self.dfs(grid, 0, 0, 0, len(grid[0]) - 1, memo)

    def dfs(self, grid, r1, c1, r2, c2, memo):
        if (r1, c1, r2, c2) in memo:
            return memo[(r1, c1, r2, c2)]

        m, n = len(grid), len(grid[0])
        cherry = 0

        # over the range
        if r1 == m or c1 == n or c1 < 0 or r2 == m or c2 == n or c2 < 0:
            return float('-inf')

        # 如果机器人1和机器人2同时走到同一个点 --> 只能摘一个地方的
        # 如果机器人1和机器人2不在同一个点 --> 摘两个地方的
        if r2 == r1 and c2 == c1:
            cherry += grid[r1][c1]
        else:
            cherry += grid[r1][c1] + grid[r2][c2]

        # stop points --> return
        if r1 == m - 1 and r2 == m - 1:
            return cherry

        cherry += max(self.dfs(grid, r1 + 1, c1 - 1, r2 + 1, c2 - 1, memo),
                      self.dfs(grid, r1 + 1, c1 - 1, r2 + 1, c2, memo),
                      self.dfs(grid, r1 + 1, c1 - 1, r2 + 1, c2 + 1, memo),
                      self.dfs(grid, r1 + 1, c1, r2 + 1, c2 - 1, memo),
                      self.dfs(grid, r1 + 1, c1, r2 + 1, c2, memo),
                      self.dfs(grid, r1 + 1, c1, r2 + 1, c2 + 1, memo),
                      self.dfs(grid, r1 + 1, c1 + 1, r2 + 1, c2 - 1, memo),
                      self.dfs(grid, r1 + 1, c1 + 1, r2 + 1, c2, memo),
                      self.dfs(grid, r1 + 1, c1 + 1, r2 + 1, c2 + 1, memo))

        memo[(r1, c1, r2, c2)] = cherry
        return memo[(r1, c1, r2, c2)]


class Solution2:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # 两个机器人摘樱桃， 一个从[0,0] 一个从[0,-1]出发，到底就停，可以左斜，向下，右斜走，问最多能摘多少樱桃

        memo = {}
        return self.dfs(grid, 0, 0, 0, len(grid[0]) - 1, memo)

    def dfs(self, grid, r1, c1, r2, c2, memo):
        if (r1, c1, r2, c2) in memo:
            return memo[(r1, c1, r2, c2)]

        m, n = len(grid), len(grid[0])

        if r1 == m and r2 == m:
            return 0

        if c1 >= n or c1 < 0 or c2 >= n or c2 < 0:
            return float('-inf')

        cherry = 0
        for x in (1, 0, -1):
            for y in (1, 0, -1):
                val = 0
                if r1 == r2 and c1 == c2:
                    val = grid[r1][c1]
                else:
                    val = grid[r1][c1] + grid[r2][c2]
                cherry = max(cherry, self.dfs(grid, r1 + 1, c1 + x, r2 + 1, c2 + y, memo) + val)

        memo[(r1, c1, r2, c2)] = cherry
        return memo[(r1, c1, r2, c2)]

