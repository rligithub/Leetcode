class Solution:  # top down dp
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}
        return self.dfs(word1, word2, 0, 0, memo)

    def dfs(self, s, t, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > len(s) - 1:
            return len(t) - j
        if j > len(t) - 1:
            return len(s) - i

        if s[i] == t[j]:
            res = self.dfs(s, t, i + 1, j + 1, memo)
        else:
            res = min(self.dfs(s, t, i + 1, j, memo), self.dfs(s, t, i, j + 1, memo),
                      self.dfs(s, t, i + 1, j + 1, memo)) + 1

        memo[(i, j)] = res
        return memo[(i, j)]