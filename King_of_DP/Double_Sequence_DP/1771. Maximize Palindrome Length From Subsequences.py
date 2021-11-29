class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        # 区间dp求最长palindrome --> 整合 word1 + word2
        m = len(word1)
        n = len(word2)
        s = word1 + word2

        memo = {}
        return self.dfs(m, s, 0, m + n - 1, False, memo)

    def dfs(self, m, s, i, j, matched, memo):
        if (i, j, matched) in memo:
            return memo[(i, j, matched)]

        # i 必须在word1中，j必须在word2中，之前子字符必须不为空
        if not matched and (i >= m or j < m):
            return 0

        if i == j:
            return 1

        if i > j:
            return 0

        if s[i] == s[j]:
            res = self.dfs(m, s, i + 1, j - 1, True, memo) + 2
        else:
            res = max(self.dfs(m, s, i + 1, j, matched, memo), self.dfs(m, s, i, j - 1, matched, memo))

        memo[(i, j, matched)] = res
        return memo[(i, j, matched)]


#class Solution2:# 双序列dp --> 求word1和word2[::-1]有几个共同子序列 + word1和word2剩余可组成的palindrome
