class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 给出每个图的path方向，求是否可以从grid左上角走到右下角

        # step1: build graph --> {street_num:{direction: connected_street_num}}
        graph = {1: {'r': [1, 3, 5], 'l': [1, 4, 6]},
                 2: {'u': [2, 3, 4], 'd': [2, 5, 6]},
                 3: {'l': [1, 4, 6], 'd': [2, 5, 6]},
                 4: {'r': [1, 3, 5], 'd': [2, 5, 6]},
                 5: {'l': [1, 4, 6], 'u': [2, 3, 4]},
                 6: {'r': [1, 3, 5], 'u': [2, 3, 4]}}

        # step2: check if it is reachable
        m, n = len(grid), len(grid[0])
        visited = set()
        return self.dfs(grid, graph, m, n, 0, 0, visited)

    def dfs(self, grid, graph, m, n, i, j, visited):
        if i == m - 1 and j == n - 1:
            return True

        visited.add((i, j))
        for dx, dy, dire in (1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l'):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                if dire in graph[grid[i][j]] and grid[x][y] in graph[grid[i][j]][dire]:
                    if self.dfs(grid, graph, m, n, x, y, visited):
                        return True
        return False


class Solution2:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 给出每个图的path方向，求是否可以从grid左上角走到右下角

        # step1: build graph --> 可以走的方向
        graph = {1: ['r', 'l'],
                 2: ['u', 'd'],
                 3: ['l', 'd'],
                 4: ['r', 'd'],
                 5: ['l', 'u'],
                 6: ['r', 'u']}

        opposite = {'l': 'r', 'r': 'l', 'u': 'd', 'd': 'u'}

        # step2: check if it is reachable
        m, n = len(grid), len(grid[0])
        visited = set()
        return self.dfs(grid, graph, opposite, m, n, 0, 0, visited)

    def dfs(self, grid, graph, opposite, m, n, i, j, visited):
        if i == m - 1 and j == n - 1:
            return True

        visited.add((i, j))

        for x, y, dire in (i + 1, j, 'd'), (i, j + 1, 'r'), (i - 1, j, 'u'), (i, j - 1, 'l'):

            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                if dire in graph[grid[i][j]] and opposite[dire] in graph[grid[x][y]]:
                    if self.dfs(grid, graph, opposite, m, n, x, y, visited):
                        return True

            # if x < 0 or x >= m or j < 0 or j >= n or (x, y) in visited or dire not in graph[grid[i][j]] or opposite[dire] not in graph[grid[x][y]]:
            #     continue
            # if self.dfs(grid, graph, opposite, m, n, x, y, visited):
            #     return True
        return False

