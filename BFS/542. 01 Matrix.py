class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 求每个cell上距离最近的0 的距离

        # for loop each 0 to update cells --> get min dist

        m, n = len(mat), len(mat[0])
        queue = collections.deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((0, i, j))
                    visited.add((i, j))

        while queue:
            dist, i, j = queue.popleft()
            mat[i][j] = dist

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and mat[x][y] != 0 and (x, y) not in visited:
                    queue.append((dist + 1, x, y))
                    visited.add((x, y))
        return mat