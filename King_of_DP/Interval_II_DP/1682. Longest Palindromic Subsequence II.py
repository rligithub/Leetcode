class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dcbccacdb --> dc cc cd --> prev index is not alway i - 1  --> should add variable "prev"

        memo = {}
        return self.dfs(s, '', 0, len(s) - 1, memo)

    def dfs(self, s, prev, i, j, memo):
        if (prev, i, j) in memo:
            return memo[(prev, i, j)]

        # must be even length, if length == 1, return 0
        if i >= j:
            return 0

        if s[i] == s[j] and s[i] != prev:
            res = self.dfs(s, s[i], i + 1, j - 1, memo) + 2
        else:
            res = max(self.dfs(s, prev, i + 1, j, memo), self.dfs(s, prev, i, j - 1, memo))

        memo[(prev, i, j)] = res
        return memo[(prev, i, j)]