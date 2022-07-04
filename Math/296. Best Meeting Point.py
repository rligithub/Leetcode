class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # 由于是求1之间的 manhattan distance，则可以分为两部分，横坐标之间的最小距离 和 纵坐标之间的最小距离
        m, n = len(grid), len(grid[0])

        # step1: collect both the row and column coordinates
        rows = []
        cols = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        # step2: sort them and select their middle elements
        i = rows[len(rows) // 2]
        cols.sort()
        j = cols[len(cols) // 2]
        # step3: calculate the total distance as the sum of two independent 1D problems
        print(rows, cols)
        return self.minDist(rows, i) + self.minDist(cols, j)

    def minDist(self, nums, origin):
        dist = 0
        for num in nums:
            dist += abs(num - origin)
        return dist