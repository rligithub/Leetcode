class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        heap = []
        heapq.heappush(heap, (0, start[0], start[1]))
        visited = set()

        while heap:
            dist, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == destination[0] and j == destination[1]:
                return dist

            for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
                x = i
                y = j
                new_dist = dist
                while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                    x += dx
                    y += dy
                    new_dist += 1
                x -= dx
                y -= dy
                new_dist -= 1
                heapq.heappush(heap, (new_dist, x, y))


        return -1


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