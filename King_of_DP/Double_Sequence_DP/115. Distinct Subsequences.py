class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 对于每个s[i]都有 选跟不选 看能不能组成 t
        memo = {}
        return self.dfs(s, t, 0, 0, memo)

    def dfs(self, s, t, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # 走完 t，算一个solution
        if j == len(t):
            return 1
            # 如果s走完，还没有解，返回0
        if i == len(s):
            return 0

            # 对于每个s中和t相同的char，都有选和不选
        if s[i] == t[j]:
            res = self.dfs(s, t, i + 1, j + 1, memo) + self.dfs(s, t, i + 1, j, memo)
        else:
            res = self.dfs(s, t, i + 1, j, memo)

        memo[(i, j)] = res
        return res