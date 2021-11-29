class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # three ways to edit --> add / delete / replace

        memo = {}
        return self.dfs(word1, word2, 0, 0, memo)

    def dfs(self, word1, word2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(word1):
            return len(word2) - j

        if j == len(word2):
            return len(word1) - i

        if word1[i] == word2[j]:
            res = self.dfs(word1, word2, i + 1, j + 1, memo)
        else:
            res = min(self.dfs(word1, word2, i + 1, j, memo), self.dfs(word1, word2, i + 1, j + 1, memo),
                      self.dfs(word1, word2, i, j + 1, memo)) + 1

        memo[(i, j)] = res
        return memo[(i, j)]



