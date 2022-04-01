class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])

        i, j = start[0], start[1]
        queue = collections.deque()
        queue.append((i, j))
        visited = set()
        visited.add((i, j))

        while queue:
            i, j = queue.popleft()
            if i == destination[0] and j == destination[1]:
                return True

            for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
                x = i
                y = j
                while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                    x = x + dx
                    y = y + dy
                xx = x - dx
                yy = y - dy
                if (xx, yy) not in visited:
                    queue.append((xx, yy))
                    visited.add((xx, yy))

        return False