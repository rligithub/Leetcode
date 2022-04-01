class Solution1:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:

        m, n = len(maze), len(maze[0])
        heap = [(0, "", ball[0], ball[1])]
        directions = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]
        memo = collections.defaultdict(list)
        memo[(ball[0], ball[1])] = [0, ""]

        while heap:
            dist, pattern, i, j = heapq.heappop(heap)
            if [i, j] == hole:
                return pattern

            for dx, dy, d in directions:
                new_dist, x, y = dist, i, j
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                    x += dx
                    y += dy
                    new_dist += 1
                    if [x, y] == hole:
                        break

                if (x, y) not in memo or [new_dist, pattern + d] < memo[(x, y)]:
                    memo[(x, y)] = [new_dist, pattern + d]
                    heapq.heappush(heap, [new_dist, pattern + d, x, y])
        return 'impossible'


class Solution2:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:

        m, n = len(maze), len(maze[0])
        heap = []
        heapq.heappush(heap, (0, '', ball[0], ball[1]))
        visited = set()

        while heap:
            dist, path, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            print(i, j)
            visited.add((i, j))
            if i == hole[0] and j == hole[1]:
                return path

            for dx, dy, dire in (1, 0, 'd'), (0, 1, 'r'), (0, -1, 'l'), (-1, 0, 'u'):
                x = i
                y = j
                new_dist = dist
                new_path = path + dire
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    new_dist += 1
                    if x == hole[0] and y == hole[1]:
                        break
                heapq.heappush(heap, (new_dist, new_path, x, y))

        return 'impossible'


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:

        m, n = len(maze), len(maze[0])
        heap = []
        heapq.heappush(heap, (0, '', ball[0], ball[1]))
        visited = set()

        while heap:
            dist, path, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            print(i, j)
            visited.add((i, j))
            if i == hole[0] and j == hole[1]:
                return path

            for dx, dy, dire in (1, 0, 'd'), (0, 1, 'r'), (0, -1, 'l'), (-1, 0, 'u'):
                x = i
                y = j
                new_dist = dist
                new_path = path + dire
                while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                    x += dx
                    y += dy
                    new_dist += 1
                    if x == hole[0] and y == hole[1]:
                        x += dx
                        y += dy
                        break
                x -= dx
                y -= dy
                new_dist -= 1
                heapq.heappush(heap, (new_dist, new_path, x, y))

        return 'impossible'
