class Solution:  # top down dp
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # triangle代替了matrix，求最小路径和。triangle的行数等于每行的个数

        memo = {}
        return self.dfs(triangle, 0, 0, memo)

    def dfs(self, triangle, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # triangle的行数等于每行的个数
        n = len(triangle)

        # stop point --> i 走到最后一行
        if i == n - 1:
            return triangle[i][j]

        # 或者 stop point --> i 走出最后一行
        # if i == n:
        #    return 0

        res = min(self.dfs(triangle, i + 1, j, memo), self.dfs(triangle, i + 1, j + 1, memo)) + triangle[i][j]

        memo[(i, j)] = res
        return memo[(i, j)]