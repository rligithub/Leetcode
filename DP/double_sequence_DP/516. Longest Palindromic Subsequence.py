class Solution:  # top down dp
    def longestPalindromeSubseq(self, s: str) -> int:
        # 最长palindromic subsequence
        # palindromic -- > reverse string s[::-1]
        # 最长 subsequence --> LCS

        memo = {}
        return self.dfs(s, s[::-1], 0, 0, memo)

    def dfs(self, s, r, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        n = len(s)
        # base case --> 任何一个走到头，停下来
        if i > n - 1 or j > n - 1:
            return 0

        if i < n and j < n and s[i] == r[j]:
            res = self.dfs(s, r, i + 1, j + 1, memo) + 1
        else:
            res = max(self.dfs(s, r, i + 1, j, memo), self.dfs(s, r, i, j + 1, memo))

        memo[(i, j)] = res
        return memo[(i, j)]

