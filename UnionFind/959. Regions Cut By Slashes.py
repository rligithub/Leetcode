class Solution:  # union find - divide by 3*3
    def regionsBySlashes(self, grid: List[str]) -> int:
        # step1: build graph
        m, n = len(grid), len(grid[0])
        graph = [[1] * 3 * n for _ in range(3 * m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '/':
                    graph[i * 3][j * 3 + 2] = 0
                    graph[i * 3 + 1][j * 3 + 1] = 0
                    graph[i * 3 + 2][j * 3] = 0

                if grid[i][j] == '\\':
                    graph[i * 3][j * 3] = 0
                    graph[i * 3 + 1][j * 3 + 1] = 0
                    graph[i * 3 + 2][j * 3 + 2] = 0

        # step2: count num of islands

        M, N = 3 * m, 3 * n
        uf = UnionFind(9 * m * n)
        for i in range(M):
            for j in range(N):
                if graph[i][j] == 1:
                    uf.count += 1
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < M and 0 <= y < N and graph[x][y] == 1:
                            uf.union(i * N + j, x * N + y)

        return uf.count


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.count = 0

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[min(rootA, rootB)] = max(rootA, rootB)
            self.count -= 1


class Solution:  # union find --> divided by 4 parts
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(n * n * 4)

        def get_pos(i, j, k):
            return (i * n + j) * 4 + k

        # 分为四个部分 --> top 0， right 1， down 2， left 3
        for i in range(n):
            for j in range(n):
                if i > 0:
                    uf.union(get_pos(i - 1, j, 2), get_pos(i, j, 0))  # connect 上下部分
                if j > 0:
                    uf.union(get_pos(i, j - 1, 1), get_pos(i, j, 3))
                if grid[i][j] == '/':
                    uf.union(get_pos(i, j, 3), get_pos(i, j, 0))
                    uf.union(get_pos(i, j, 1), get_pos(i, j, 2))
                elif grid[i][j] == '\\':
                    uf.union(get_pos(i, j, 1), get_pos(i, j, 0))
                    uf.union(get_pos(i, j, 3), get_pos(i, j, 2))
                elif grid[i][j] == ' ':
                    uf.union(get_pos(i, j, 0), get_pos(i, j, 1))
                    uf.union(get_pos(i, j, 1), get_pos(i, j, 2))
                    uf.union(get_pos(i, j, 2), get_pos(i, j, 3))

        return uf.count


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.count = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
            self.count -= 1
