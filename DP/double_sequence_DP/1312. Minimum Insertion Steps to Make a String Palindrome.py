class Solution1:
    def minInsertions(self, s: str) -> int:
        # 最少增加几个steps 使得string变成palindrome
        # 增加steps --> Shortest common superstring
        # 变成palindrome --> compare to reverse string s[::-1]

        n = len(s)
        r = s[::-1]
        print(r)
        # dp[i][j] --> shortest common superstring of s[:i] and r[:j]

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i
            dp[0][i] = i

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == r[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1] - n


class Solution:
    def minInsertions(self, s: str) -> int:
        r = s[::-1]
        memo = {}
        return self.dfs(s, r, 0, 0, memo) - len(s)

    def dfs(self, s, r, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        n = len(s)
        if i > n - 1:
            return n - j

        if j > n - 1:
            return n - i

        if i == n and j == n:
            return 0

        if s[i] == r[j]:
            res = self.dfs(s, r, i + 1, j + 1, memo) + 1
        else:
            res = min(self.dfs(s, r, i + 1, j, memo) + 1, self.dfs(s, r, i, j + 1, memo) + 1)

        memo[(i, j)] = res
        return memo[(i, j)]


