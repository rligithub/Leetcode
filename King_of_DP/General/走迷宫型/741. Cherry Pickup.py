class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # 摘樱桃 --> 从[0,0]走到[-1，-1]，再从[-1,-1]走回[0,0]， 求走一个来回最多能摘多少樱桃
        # 相当于两个人一起从原点出发到终点，求两个人最后摘的樱桃总数
        # if grid[i][j] == -1: unwalkable --> return float('-inf')

        memo = {}
        # if no valid path, return 0
        return max(0, self.dfs(grid, 0, 0, 0, 0, memo))

    def dfs(self, grid, x1, y1, x2, y2, memo):
        if (x1, y1, x2, y2) in memo:
            return memo[(x1, y1, x2, y2)]

        m, n = len(grid), len(grid[0])
        res = 0

        if x1 >= n or y1 >= m or x2 >= n or y2 >= m or grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return float('-inf')

        # 第一个人摘了樱桃
        if grid[x1][y1] == 1:
            res += 1
        # 第二个人 如果走到第一个人走过的地方，就没有樱桃了。只能走到还未被摘过的樱桃那摘樱桃
        if grid[x2][y2] == 1 and x1 != x2 and y1 != y2:
            res += 1

        # 两个人出发的路程是一样的 x1 + y1 = x2 + y2 可简化为三维
        if x1 == n - 1 and y1 == m - 1 and x2 == n - 1 and y2 == m - 1:
            return res

        res += max(self.dfs(grid, x1 + 1, y1, x2 + 1, y2, memo),
                   self.dfs(grid, x1 + 1, y1, x2, y2 + 1, memo),
                   self.dfs(grid, x1, y1 + 1, x2 + 1, y2, memo),
                   self.dfs(grid, x1, y1 + 1, x2, y2 + 1, memo))

        memo[(x1, y1, x2, y2)] = res
        return memo[(x1, y1, x2, y2)]