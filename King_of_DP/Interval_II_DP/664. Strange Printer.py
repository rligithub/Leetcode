class Solution:
    def strangePrinter(self, s: str) -> int:
        # 类似moved box
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        # 不覆盖 打印
        res = self.dfs(s, i + 1, j, memo) + 1

        # 覆盖打印
        for k in range(i + 1, j + 1):
            if s[i] == s[k]:
                res = min(res, self.dfs(s, i, k - 1, memo) + self.dfs(s, k + 1, j, memo))
        memo[(i, j)] = res
        return res





