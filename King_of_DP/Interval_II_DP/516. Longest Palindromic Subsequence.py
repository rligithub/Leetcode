class Solution:  # top down dp +  区间dp
    def longestPalindromeSubseq(self, s: str) -> int:
        # 最长回文字符串 --> 不连续区间
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        if s[i] == s[j]:
            res = self.dfs(s, i + 1, j - 1, memo) + 2
        else:
            res = max(self.dfs(s, i + 1, j, memo), self.dfs(s, i, j - 1, memo))

        memo[(i, j)] = res
        return memo[(i, j)]