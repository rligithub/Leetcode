class Solution1:  # TLE
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[start[0]][start[1]] = 0
        visited = set()
        i, j = start[0], start[1]
        self.dfs(maze, m, n, i, j, destination, dist)

        if dist[destination[0]][destination[1]] != float('inf'):
            return dist[destination[0]][destination[1]]
        else:
            return -1

    def dfs(self, maze, m, n, i, j, destination, dist):

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i
            y = j
            steps = 0
            while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                x += dx
                y += dy
                steps += 1
            x -= dx
            y -= dy
            steps -= 1
            update_dist = dist[i][j] + steps

            if dist[x][y] > update_dist:
                dist[x][y] = update_dist
                self.dfs(maze, m, n, x, y, destination, dist)


class Solution2:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        m, n = len(maze), len(maze[0])
        heap = [(0, start[0], start[1])]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        memo = collections.defaultdict(int)
        memo[(start[0], start[1])] = 0

        while heap:
            dist, i, j = heapq.heappop(heap)
            if [i, j] == destination:
                return dist

            for dx, dy in directions:
                new_dist, x, y = dist, i, j
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    new_dist += 1

                if (x, y) not in memo or new_dist < memo[(x, y)]:
                    memo[(x, y)] = new_dist
                    heapq.heappush(heap, [new_dist, x, y])
        return -1


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        m, n = len(maze), len(maze[0])
        heap = []
        heapq.heappush(heap, (0, start[0], start[1]))

        visited = set()

        while heap:
            dist, i, j = heapq.heappop(heap)

            if (i, j) in visited:  # check dist (with heap) and visited together
                continue
            visited.add((i, j))

            if [i, j] == destination:
                return dist

            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                new_dist, x, y = dist, i, j
                while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                    x += dx
                    y += dy
                    new_dist += 1
                x -= dx
                y -= dy
                new_dist -= 1

                heapq.heappush(heap, (new_dist, x, y))
        return -1


