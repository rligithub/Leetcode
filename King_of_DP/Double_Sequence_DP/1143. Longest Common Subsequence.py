class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.dfs(text1, text2, 0, 0, memo)

    def dfs(self, text1, text2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            res = self.dfs(text1, text2, i + 1, j + 1, memo) + 1
        else:
            res = max(self.dfs(text1, text2, i, j + 1, memo), self.dfs(text1, text2, i + 1, j, memo))

        memo[(i, j)] = res
        return res