class Solution2:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        uf = UnionFind()

        # 先敲砖
        for i, j in hits:
            grid[i][j] -= 1

        # 添加天花板, 将最上层的和天花板合并
        top = -1
        for j in range(n):
            if grid[0][j] == 1:
                uf.union(top, j)

        # 遍历所有砖块 尝试合并这些连通分量
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        uf.union(i * n + j, x * n + y)
        res = []
        for i, j in hits[::-1]:
            grid[i][j] += 1  # 恢复砖块
            if grid[i][j] != 1:  # 说明之前不是砖块
                res.append(0)
                continue

            after_hit = uf.size[uf.find(top)]

            for dx, dy in (0, -1), (0, 1), (-1, 0), (1, 0):
                x, y = i + dx, j + dy
                if (0 <= x < m) and (0 <= y < n) and grid[x][y] == 1:
                    uf.union(i * n + j, x * n + y)
            if i == 0:
                uf.union(top, i * n + j)

            before_hit = uf.size[uf.find(top)]
            root = uf.find(i * n + j)
            p = uf.find(top)
            if root == p:
                res.append(before_hit - after_hit - 1)
            else:
                res.append(before_hit - after_hit)

        return res[::-1]


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, i):
        if i not in self.size:
            self.size[i] = 1

        if i not in self.parent:
            self.parent[i] = i
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]

