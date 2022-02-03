class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 水流只能按照上、下、左、右四个方向流动, 找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标
        # 四个方向 找 水流能到的地方 --> 找 左上 和 右下的交集
        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        for i in range(m):
            self.dfs(heights, i, 0, pacific)  # down
            self.dfs(heights, i, n - 1, atlantic)  # up
        for j in range(n):
            self.dfs(heights, 0, j, pacific)  # left
            self.dfs(heights, m - 1, j, atlantic)  # right

        res = []
        for point in pacific:
            if point in atlantic:
                res.append(point)
        return res

    def dfs(self, heights, i, j, visited):
        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            ii = i + dx
            jj = j + dy
            if 0 <= ii < len(heights) and 0 <= jj < len(heights[0]) and (ii, jj) not in visited and heights[i][j] <= \
                    heights[ii][jj]:
                self.dfs(heights, ii, jj, visited)





