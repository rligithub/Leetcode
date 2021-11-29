class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(s), len(p)

        if i == m and j == n:
            return True

        if i < m and j == n:
            return False

        if i > m:
            return False

        if j < n and p[j] == '*':
            if self.dfs(s, p, i + 1, j, memo) or self.dfs(s, p, i, j + 1, memo):
                memo[(i, j)] = True
                return True

        if i < m and j < n and s[i] == p[j] or p[j] == '?':
            if self.dfs(s, p, i + 1, j + 1, memo):
                memo[(i, j)] = True
                return True
        memo[(i, j)] = False
        return False

