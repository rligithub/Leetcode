class Solution:  # TLE
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # 每过一天就有一块land变成water，求能够从 top 走到bottom的最后一天

        # build graph
        graph = [[0] * col for _ in range(row)]

        for day in range(len(cells)):
            i, j = cells[day]
            graph[i - 1][j - 1] = 1  # given a 1-based 2D array cells
            can_pass = False
            visited = set()
            for j in range(col):
                if graph[0][j] == 1:
                    continue
                if self.dfs(graph, row, col, 0, j, visited):
                    can_pass = True
                    break

            if can_pass == False:
                return day

    def dfs(self, graph, m, n, i, j, visited):
        if i == m - 1:
            return True

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and graph[x][y] == 0:
                if self.dfs(graph, m, n, x, y, visited):
                    return True
        return False


class Solution1:  # Binary search + dfs
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        left, right = 0, len(cells) - 1

        while left <= right:
            mid = left + (right - left) // 2

            graph = [[0] * col for _ in range(row)]
            self.fill(graph, cells, mid)

            can_pass = False
            visited = set()
            for j in range(col):

                if graph[0][j] == 0 and self.dfs(graph, row, col, 0, j, visited):
                    can_pass = True
                    break

            if can_pass:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def fill(self, graph, cells, mid):
        for d in range(mid + 1):
            i, j = cells[d]
            graph[i - 1][j - 1] = 1  # given a 1-based 2D array cells

    def dfs(self, graph, m, n, i, j, visited):
        if i == m - 1:
            return True

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and graph[x][y] == 0:
                if self.dfs(graph, m, n, x, y, visited):
                    return True
        return False


class Solution2:  # Binary search + dfs
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        left, right = 0, len(cells) - 1

        while left <= right:
            mid = left + (right - left) // 2

            graph = [[0] * col for _ in range(row)]
            self.fill(graph, cells, mid)

            can_pass = False
            for j in range(col):
                if graph[0][j] == 0 and self.dfs(graph, row, col, 0, j):
                    can_pass = True
                    break

            if can_pass:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def fill(self, graph, cells, mid):
        for d in range(mid + 1):
            i, j = cells[d]
            graph[i - 1][j - 1] = 1  # given a 1-based 2D array cells

    def dfs(self, graph, m, n, i, j):
        if i == m - 1:
            return True

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and graph[x][y] == 0:
                graph[x][y] = '#'
                if self.dfs(graph, m, n, x, y):
                    return True
        return False
