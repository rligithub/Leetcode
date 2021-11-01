class Solution:  # bottom up dp - TLE
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # 最短公共 母序列

        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        # print path
        path = []
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                path.append(str1[i - 1])
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] == dp[i][j]:
                    path.append(str1[i - 1])
                    i -= 1
                elif dp[i][j - 1] == dp[i][j]:
                    path.append(str2[j - 1])
                    j -= 1

        return path[::-1]