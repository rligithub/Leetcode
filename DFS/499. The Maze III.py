class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # 迷宫 --> 把ball打到hole里，打印出最短路径 -- > BFS

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








