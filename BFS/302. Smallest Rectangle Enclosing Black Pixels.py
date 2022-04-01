class Solution:  # BFS
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # maintain minX, minY, maxX, maxY for each point
        minX = x
        maxX = x
        minY = y
        maxY = y
        m, n = len(image), len(image[0])
        queue = collections.deque()
        queue.append((x, y))
        visited = set()
        visited.add((x, y))

        while queue:
            i, j = queue.popleft()
            minX = min(minX, i)
            maxX = max(maxX, i)
            minY = min(minY, j)
            maxY = max(maxY, j)

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                ii = i + dx
                jj = j + dy
                if 0 <= ii < m and 0 <= jj < n and image[ii][jj] == '1' and (ii, jj) not in visited:
                    queue.append((ii, jj))
                    visited.add((ii, jj))

        return (maxX - minX + 1) * (maxY - minY + 1)
