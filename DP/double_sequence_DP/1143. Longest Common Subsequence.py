class Solution:  # top down dp
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.dfs(text1, text2, 0, 0, memo)

    def dfs(self, s, t, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > len(s) - 1 or j > len(t) - 1:
            return 0

        if s[i] == t[j]:
            res = self.dfs(s, t, i + 1, j + 1, memo) + 1
        else:
            res = max(self.dfs(s, t, i + 1, j, memo), self.dfs(s, t, i, j + 1, memo))

        memo[(i, j)] = res
        return res
