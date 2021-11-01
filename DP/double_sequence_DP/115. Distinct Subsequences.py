class Solution:  # top down dp
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        return self.dfs(s, t, 0, 0, memo)

    def dfs(self, s, t, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # 短短走到头，结束一个solution， +1
        if j > len(t) - 1:
            return 1

        # 长长走到头，没有solution
        if i > len(s) - 1:
            return 0

        if s[i] == t[j]:
            res = self.dfs(s, t, i + 1, j + 1, memo) + self.dfs(s, t, i + 1, j, memo)
        else:
            res = self.dfs(s, t, i + 1, j, memo)

        memo[(i, j)] = res
        return memo[(i, j)]