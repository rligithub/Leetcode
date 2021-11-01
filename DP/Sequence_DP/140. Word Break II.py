class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}
        res = []

        res = self.dfs(s, wordDict, 0, memo)
        return [" ".join(words) for words in res]

    def dfs(self, s, dicts, pos, memo):
        if pos in memo:
            return memo[pos]

        if pos == len(s):
            return [[]]

        res = []
        for end in range(pos + 1, len(s) + 1):
            if s[pos:end] in dicts:
                for substr in self.dfs(s, dicts, end, memo):
                    res.append([s[pos:end]] + substr)

        memo[pos] = res
        return res

