class Solution3:  # - union find
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if m <= 2 or n <= 2:
            return
        uf = UnionFind(m * n + 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        uf.union(i * n + j, m * n)
                    else:
                        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                            x = i + dx
                            y = j + dy
                            if board[x][y] == 'O':
                                uf.union(i * n + j, x * n + y)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and uf.find(i * n + j) != m * n:
                    board[i][j] = 'X'


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parent[min(rootA, rootB)] = max(rootA, rootB)  # 有方向性， 确定哪个在前哪个在后

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]


class Solution:  # union find
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        parent = {}

        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        dummy = m * n

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        self.union(parent, i * n + j, dummy)  # need to be remained O
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":  # union all connected O
                                self.union(parent, i * n + j, (i + x) * n + (j + y))
        for i in range(m):
            for j in range(n):
                if dummy == self.find(parent, i * n + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

    def find(self, parent, x):
        parent.setdefault(x, x)
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, a, b):
        rootA = self.find(parent, a)
        rootB = self.find(parent, b)
        if rootA != rootB:
            parent[min(rootA, rootB)] = max(rootA, rootB)