class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # 求 ball 是否能到 destination ---> 不碰到墙就会一直滚，求最后停下来的地方是不是为destination
        m, n = len(maze), len(maze[0])
        visited = set()
        i, j = start[0], start[1]
        return self.dfs(maze, m, n, i, j, destination, visited)

    def dfs(self, maze, m, n, i, j, destination, visited):
        if i == destination[0] and j == destination[1]:
            return True

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i
            y = j
            # rolling to the same direction if not hit wall or out of range
            while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                x = x + dx
                y = y + dy
            xx = x - dx  # back to prev position
            yy = y - dy  # back to prev position
            if (xx, yy) not in visited:
                if self.dfs(maze, m, n, xx, yy, destination, visited):
                    return True

