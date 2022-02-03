class Solution1:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # maintain minX, minY, maxX, maxY for each point
        self.minX, self.maxX = x, x
        self.minY, self.maxY = y, y

        visited = set()
        self.dfs(image, x, y, visited)
        return (self.maxX - self.minX + 1) * (self.maxY - self.minY + 1)

    def dfs(self, image, x, y, visited):
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or (x, y) in visited or image[x][y] != '1':
            return

        visited.add((x, y))
        self.minX = min(self.minX, x)
        self.minY = min(self.minY, y)
        self.maxX = max(self.maxX, x)
        self.maxY = max(self.maxY, y)

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            self.dfs(image, x + dx, y + dy, visited)


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # maintain minX, minY, maxX, maxY for each point
        self.minX, self.maxX = x, x
        self.minY, self.maxY = y, y

        visited = set()
        self.dfs(image, x, y, visited)
        return (self.maxX - self.minX + 1) * (self.maxY - self.minY + 1)

    def dfs(self, image, x, y, visited):

        visited.add((x, y))
        self.minX = min(self.minX, x)
        self.minY = min(self.minY, y)
        self.maxX = max(self.maxX, x)
        self.maxY = max(self.maxY, y)

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            xx = x + dx
            yy = y + dy
            if 0 <= xx < len(image) and 0 <= yy < len(image[0]) and (xx, yy) not in visited and image[xx][yy] == '1':
                self.dfs(image, xx, yy, visited)
