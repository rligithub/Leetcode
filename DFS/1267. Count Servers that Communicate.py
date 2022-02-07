class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # 有几个servers可以相互呼叫 --> 同行或者同列的都可以， 两个同行以上或者两个同列以上 count ++

        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row[i] >= 2 or col[j] >= 2):
                    count += 1
        return count


