class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 给一个string和dict，看能否把string分成几个单词在dict里

        # memo --> substring from index i to index j, if substring is in dict
        memo = {}
        wordDict = set(wordDict)
        return self.dfs(s, wordDict, 0, memo)

    def dfs(self, s, dicts, start, memo):
        if start in memo:
            return memo[start]

        # base case
        if start > len(s) - 1:
            return True

            # 看 后k个数的位置 有没有一个满足条件
        for end in range(start + 1, len(s) + 1):
            # print()
            if (s[start: end] in dicts) and self.dfs(s, dicts, end, memo):
                memo[start] = True
                return True

        memo[start] = False
        return False


class Solution2:  # bottom up dp
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        if not wordDict:
            return False

        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]











