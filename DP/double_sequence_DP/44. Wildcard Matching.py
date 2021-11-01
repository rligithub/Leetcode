class Solution:  # top down dp
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(s), len(p)

        # base case --> 都走到头
        if i == m and j == n:
            return True

            # base case --> pattern走完了，但是string没走完
        if i < m and j == n:
            return False

            # base case --> string走完了
        if i > m:
            return False

        if i < m and j < n and (s[i] == p[j] or p[j] == '?'):
            if self.dfs(s, p, i + 1, j + 1, memo):
                memo[(i, j)] = True
                return True
        if j < n and p[j] == '*':
            if (self.dfs(s, p, i + 1, j, memo) or self.dfs(s, p, i, j + 1, memo)):
                memo[(i, j)] = True
                return True

        memo[(i, j)] = False
        return False


class Solution1:  # bottom up dp
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # * ---> empty; compare j - 1 vs. i
                    # * ---> more letters; compare j vs i -1
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[-1][-1]