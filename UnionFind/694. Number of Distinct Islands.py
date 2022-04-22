class Solution:  # union find
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # union
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            uf.union(i * n + j, x * n + y)

        # find + build graph to record all nodes with same root --> {root1: position1, postion2}
        graph = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    root = uf.find(i * n + j)
                    graph[root].append(i * n + j)

        # for loop graph(each root) --> convert position back to (x, y), record path for each root --> add to set --> num of diff path
        visited = set()
        for node in graph:
            path = ''
            start_x = node // n
            start_y = node % n
            for ch in graph[node]:
                x = ch // n
                y = ch % n
                path += str(x - start_x) + str(y - start_y)  # row + col
            visited.add(path)
        return len(visited)


class UnionFind():
    def __init__(self, n):
        self.parent = {i: i for i in range(n + 1)}

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[max(rootA, rootB)] = min(rootA, rootB)
