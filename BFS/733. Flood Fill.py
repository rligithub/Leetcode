class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        old_color = image[sr][sc]
        queue = collections.deque()
        queue.append((sr, sc))
        visited = set()
        visited.add((sr, sc))

        while queue:
            i, j = queue.popleft()
            image[i][j] = newColor
            for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and image[x][y] == old_color:
                    queue.append((x, y))
                    visited.add((x, y))

        return image