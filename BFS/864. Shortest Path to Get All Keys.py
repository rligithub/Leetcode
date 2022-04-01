class Solution:
    def shortestPathAllKeys(self, grid):
        m, n = len(grid), len(grid[0])

        queue = collections.deque()
        visited = set()

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    queue.append((i, j, 0, 0))
                elif grid[i][j].islower():
                    count += 1

        fullmask = (1 << count) - 1

        while queue:
            i, j, mask, dist = queue.popleft()

            if mask == fullmask:
                return dist

            for dx, dy in (0, 1), (0, -1), (-1, 0), (1, 0):
                x = i + dx
                y = j + dy
                nxtmask = mask
                if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                    if grid[x][y] in "ABCDEF":
                        k = ord(grid[x][y]) - ord('A')
                        if mask & (1 << k) == 0:
                            continue
                    elif grid[x][y] in "abcdef":
                        k = ord(grid[x][y]) - ord('a')
                        nxtmask = mask | (1 << k)
                    if (x, y, nxtmask) not in visited:
                        queue.append((x, y, nxtmask, dist + 1))
                        visited.add((x, y, nxtmask))

        return -1