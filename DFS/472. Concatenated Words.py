class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # similar to word break 1 and word break 2
        dictionary = set(words)

        res = []

        for word in words:
            if not word:
                continue
            if self.dfs(word, dictionary, 0, {}):
                res.append(word)
        return res

    def dfs(self, word, dictionary, i, memo):
        if i in memo:
            return memo[i]
        if i > len(word) - 1:
            return True

        for k in range(i + 1, len(word) + 1):

            if word[i:k] != word and (word[i:k] in dictionary):
                if self.dfs(word, dictionary, k, memo):
                    memo[i] = True
                    return memo[i]
        memo[i] = False
        return False


