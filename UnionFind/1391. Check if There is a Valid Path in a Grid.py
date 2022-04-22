class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 给出每个图的path方向，求是否可以从grid左上角走到右下角

        # step1: build graph --> {street_num:{direction: connected_street_num}}
        graph = {
            1: {'l': [1, 4, 6], 'r': [1, 3, 5]},
            2: {'u': [2, 3, 4], 'd': [2, 5, 6]},
            3: {'l': [1, 4, 6], 'd': [2, 5, 6]},
            4: {'r': [1, 3, 5], 'd': [2, 5, 6]},
            5: {'l': [1, 4, 6], 'u': [2, 3, 4]},
            6: {'u': [2, 3, 4], 'r': [1, 3, 5]}
        }

        uf = UnionFind()
        m, n = len(grid), len(grid[0])
        start = 0  # (0, 0)
        end = (m - 1) * n + n - 1  # (m-1, n-1)

        for i in range(m):
            for j in range(n):
                for dx, dy, dire in (1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l'):
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n and dire in graph[grid[i][j]] and grid[x][y] in graph[grid[i][j]][
                        dire]:
                        uf.union(i * n + j, x * n + y)
                if uf.find(start) == uf.find(end):
                    return True
        return False


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i

        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
