class Solution:  # top down + top down ---> slow
    def checkPartitioning(self, s: str) -> bool:
        dp = {}

        memo = {}
        return self.dfs(s, dp, 0, 3, memo)

    def dfs(self, s, dp, i, k, memo):
        if (i, k) in memo:
            return memo[(i, k)]

        if i == len(s) and k == 0:
            return True

        if i == len(s) or k == 0:
            return False

        for j in range(i, len(s)):
            if self.isPal(s, i, j, dp):
                if self.dfs(s, dp, j + 1, k - 1, memo):
                    memo[(i, k)] = True
                    return True

        memo[(i, k)] = False
        return False

    def isPal(self, s, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]

        if i >= j:
            return True

        if s[i] != s[j]:
            return False

        if self.isPal(s, i + 1, j - 1, dp):
            dp[(i, j)] = True
            return True

        dp[(i, j)] = False
        return False


class Solution2:  # bottom up + top down
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j or i + 1 == j:
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    dp[i][j] = True if dp[i + 1][j - 1] and s[i] == s[j] else False

        memo = {}
        return self.dfs(s, dp, 0, 3, memo)

    def dfs(self, s, dp, i, k, memo):
        if (i, k) in memo:
            return memo[(i, k)]

        if i == len(s) and k == 0:
            return True

        if i == len(s) or k == 0:
            return False

        for j in range(i, len(s)):
            if dp[i][j]:
                if self.dfs(s, dp, j + 1, k - 1, memo):
                    memo[(i, k)] = True
                    return True

        memo[(i, k)] = False
        return False


class Solution3:
    def checkPartitioning(self, s: str) -> bool:

        memo = {}
        return self.dfs(s, 0, 3, memo)

    def dfs(self, s, i, k, memo):
        if (i, k) in memo:
            return memo[(i, k)]

        n = len(s)
        if i >= n and k == 0:
            return True

        if i >= n or k == 0:
            return False

        for j in range(i, n):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                if self.dfs(s, j + 1, k - 1, memo):
                    memo[(i, k)] = True
                    return True

        memo[(i, k)] = False
        return False
