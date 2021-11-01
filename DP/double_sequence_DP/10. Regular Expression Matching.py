class Solution1:  # bottom up dp
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
                    dp[i][j] |= dp[i][j - 2]
        return dp[-1][-1]


class Solution:  # top down dp
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > len(s) - 1 and j > len(p) - 1:
            return True

        if self.matched(s, p, i, j) and self.dfs(s, p, i + 1, j + 1, memo):
            memo[(i, j)] = True
            return True
        if j + 1 < len(p) and p[j + 1] == '*':
            if self.matched(s, p, i, j) and self.dfs(s, p, i + 1, j, memo) or self.dfs(s, p, i, j + 2, memo):
                memo[(i, j)] = True
                return True
        memo[(i, j)] = False
        return False

    def matched(self, s, p, i, j):
        if i > len(s) - 1 or j > len(p) - 1:
            return False
        return s[i] == p[j] or p[j] == '.'

