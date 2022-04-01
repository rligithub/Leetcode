class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # step1: build graph
        m, n = len(grid), len(grid[0])

        graph = [[0] * 3 * n for _ in range(3 * m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '/':
                    graph[3 * i][3 * j + 2] = 1
                    graph[3 * i + 1][3 * j + 1] = 1
                    graph[3 * i + 2][3 * j] = 1
                elif grid[i][j] == '\\':
                    graph[3 * i][3 * j] = 1
                    graph[3 * i + 1][3 * j + 1] = 1
                    graph[3 * i + 2][3 * j + 2] = 1

        # step2: count how many islands
        queue = collections.deque()
        visited = set()
        count = 0
        for i in range(3 * m):
            for j in range(3 * n):
                if graph[i][j] == 0 and (i, j) not in visited:
                    self.bfs(graph, 3 * m, 3 * n, queue, visited, i, j)
                    count += 1
        return count

    def bfs(self, graph, m, n, queue, visited, i, j):

        queue.append((i, j))
        visited.add((i, j))

        while queue:

            i, j = queue.popleft()

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and graph[x][y] == 0:
                    queue.append((x, y))
                    visited.add((x, y))

