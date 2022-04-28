class Solution:  # union find
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        uf = UnionFind()

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n and grid2[x][y] == 1:
                            uf.union(i * n + j, x * n + y)

        # 记录岛屿根节点
        rootset = set()
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    root = uf.find(i * n + j)
                    rootset.add(root)

        # 2中岛屿 1中海洋 则剔除根节点
        for i in range(m):
            for j in range(n):
                p = uf.find(i * n + j)
                if p in rootset and grid1[i][j] == 0:
                    rootset.remove(p)
        # 返回树的棵树
        return len(rootset)


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



