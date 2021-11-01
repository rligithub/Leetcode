class Solution1:  # top down dp  + 双序列
    def longestPalindromeSubseq(self, s: str) -> int:
        # 最长palindromic subsequence
        # palindromic -- > reverse string s[::-1]
        # 最长 subsequence --> LIS

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


class Solution:  # top down dp +  区间dp
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # base case --> length = 1
        if i == j:
            return 1

            # base case --> length = 0
        if i > j:
            return 0

        if s[i] == s[j]:
            res = self.dfs(s, i + 1, j - 1, memo) + 2
        else:
            res = max(self.dfs(s, i + 1, j, memo), self.dfs(s, i, j - 1, memo))

        memo[(i, j)] = res

        return memo[(i, j)]




