class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # use min-heap + BFS
        # 农村包围城市
        # 把所有外围的height放到heap里，pop掉最小值，维持一个maxheight
        # 检查pop的值的四周，把周围的值放入heap里
        # if height[i][j] >= maxheight --> do nothing, can't trap water
        # if height[i][j] < maxheight --> calculate water = maxheight - height[i][j]

        if not heightMap:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        res = 0

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1  # mark visited

        maxheight = float('-inf')

        while heap:
            cur, i, j = heapq.heappop(heap)

            maxheight = max(maxheight, cur)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and heightMap[x][y] != -1:
                    if heightMap[x][y] < maxheight:
                        res += maxheight - heightMap[x][y]
                    heapq.heappush(heap, (heightMap[x][y], x, y))
                    heightMap[x][y] = -1
        return res