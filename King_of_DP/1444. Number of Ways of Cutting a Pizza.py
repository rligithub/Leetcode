class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])

        prefsum = [[0] * (n + 1) for _ in range(m + 1)]

        # prefix sum of # of apples in lower right corner
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                prefsum[i][j] = (pizza[i][j] == 'A') + prefsum[i + 1][j] + prefsum[i][j + 1] - prefsum[i + 1][j + 1]

        memo = {}
        return self.dfs(prefsum, k - 1, 0, 0, memo)

    def dfs(self, prefsum, cut, i, j, memo):
        if (cut, i, j) in memo:
            return memo[(cut, i, j)]

        if cut == 0:
            if prefsum[i][j] > 0:
                return 1
            else:
                return 0

        mod = 10 ** 9 + 7
        res = 0
        for x in range(i, len(prefsum)):
            if prefsum[i][j] > prefsum[x][j]:
                res += self.dfs(prefsum, cut - 1, x, j, memo)

        for y in range(j, len(prefsum[0])):
            if prefsum[i][j] > prefsum[i][y]:
                res += self.dfs(prefsum, cut - 1, i, y, memo)

        memo[(cut, i, j)] = res % mod
        return memo[(cut, i, j)]