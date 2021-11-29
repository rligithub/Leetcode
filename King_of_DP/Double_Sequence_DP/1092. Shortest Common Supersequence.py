class Solution:  # TLE
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # 找出最短公共祖先的长度
        # 反推出path
        memo = {}
        return self.dfs(str1, str2, 0, 0, memo)

    def dfs(self, str1, str2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(str1):
            return str2[j:]

        elif j == len(str2):
            return str1[i:]

        if str1[i] == str2[j]:
            res = str1[i] + self.dfs(str1, str2, i + 1, j + 1, memo)
        else:
            p1 = str1[i] + self.dfs(str1, str2, i + 1, j, memo)
            p2 = str2[j] + self.dfs(str1, str2, i, j + 1, memo)
            if len(p1) < len(p2):
                res = p1
            else:
                res = p2

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution2:  # bottom up dp
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # 最短公共 母序列 --> 先找出 公共最长子序列， 反推出path
        # 如果dp和前一个dp相等，则说明char不同，打印出对应的char
        # 如果dp和前一个dp都不相等，则说明char相同，打印出对应的char

        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp)
        # print path
        i, j = m, n
        res = ''
        while i > 0 or j > 0:
            print(res)
            if i > 0 and dp[i][j] == dp[i - 1][j]:
                i -= 1
                res = str1[i] + res
            elif j > 0 and dp[i][j] == dp[i][j - 1]:
                j -= 1
                res = str2[j] + res
            else:
                i -= 1
                j -= 1
                res = str1[i] + res

        return res


class Solution3:  # bottom up dp
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # 最短公共 母序列 --> 找出最长公共祖先 ， 反推path

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
        path = ''
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                path = str1[i - 1] + path
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j] + 1:
                path = str1[i - 1] + path
                i -= 1
            else:
                path = str2[j - 1] + path
                j -= 1
        while i > 0:
            path = str1[i - 1] + path
            i -= 1
        while j > 0:
            path = str2[j - 1] + path
            j -= 1

        return path