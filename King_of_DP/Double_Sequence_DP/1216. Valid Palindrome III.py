class Solution1:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # 双序列dp --> 求最长公共子序列，比较个数和k
        memo = {}
        LIC = self.dfs(s, s[::-1], 0, 0, memo)
        return len(s) - LIC <= k

    def dfs(self, s, t, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s) or j == len(s):
            return 0

        if s[i] == t[j]:
            res = self.dfs(s, t, i + 1, j + 1, memo) + 1
        else:
            res = max(self.dfs(s, t, i + 1, j, memo), self.dfs(s, t, i, j + 1, memo))

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # 区间dp，求有几个不同char
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo) <= k

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        if s[i] == s[j]:
            res = self.dfs(s, i + 1, j - 1, memo)
        else:
            res = min(self.dfs(s, i + 1, j, memo), self.dfs(s, i, j - 1, memo)) + 1

        memo[(i, j)] = res
        return memo[(i, j)]





