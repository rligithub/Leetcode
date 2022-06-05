class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)
        memo = {}

        res = 0
        for word in words:
            res = max(res, self.dfs(words, word, memo))

        return res

    def dfs(self, words, word, memo):
        if word in memo:
            return memo[word]

        res = 1
        for i in range(len(word)):
            prev = word[:i] + word[i + 1:]
            if prev in words:
                res = max(res, 1 + self.dfs(words, prev, memo))

        memo[word] = res
        return memo[word]
