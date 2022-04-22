class Solution1:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)
        board = [[0] * n for _ in range(m)]

        res = []
        visited = set()
        for i, j in positions:
            if (i, j) in visited:
                res.append(res[-1])
                continue
            visited.add((i, j))

            board[i][j] = 1
            uf.count += 1
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
                    uf.union(i * n + j, x * n + y)
            res.append(uf.count)
        return res


class UnionFind():
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
            self.count -= 1  # connected


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m * n)
        board = [[0] * n for _ in range(m)]

        res = []
        for i, j in positions:
            board[i][j] = 1
            uf.set_parent(i * n + j)
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
                    uf.union(i * n + j, x * n + y)
            res.append(uf.count)
        return res


class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(1, n + 1)]  # don't know why there is padding. If no padding, fail
        self.count = 0

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[min(rootA, rootB)] = max(rootA, rootB)
            self.count -= 1  # connected

    def set_parent(self, i):  # check if duplicated value
        if self.parent[i] == i:
            return
        self.parent[i] = i
        self.count += 1