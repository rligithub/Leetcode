class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 色块 重新粉刷颜色
        if image[sr][sc] == newColor:  # if oldcolor == newcolor
            return image

        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image

    def dfs(self, image, i, j, oldColor, newColor):
        image[i][j] = newColor

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == oldColor:
                self.dfs(image, x, y, oldColor, newColor)