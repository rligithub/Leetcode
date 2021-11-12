class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # 把str分成k份，可以把substring中的字符替换，使得每个substring都是palindrome， 求最少需要换几个字符

        # 找每个substring里有几个不同的字符 需要被替换
        dp = {}
        self.costs(s, 0, len(s) - 1, dp)

        memo = {}
        return self.dfs(s, 0, k, dp, memo)

    def costs(self, s, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]

        if i >= j:
            return 0

        res = 0
        if s[i] == s[j]:
            res = self.costs(s, i + 1, j - 1, dp)
        else:
            res = self.costs(s, i + 1, j - 1, dp) + 1

        dp[(i, j)] = res
        return res

    def dfs(self, s, i, k, dp, memo):
        if (i, k) in memo:
            return memo[(i, k)]

        if i == len(s) and k == 0:
            return 0

        if i == len(s) or k == 0:
            return float('inf')

        res = float('inf')
        for j in range(i, len(s)):
            res = min(res, self.dfs(s, j + 1, k - 1, dp, memo) + self.costs(s, i, j, dp))
        memo[(i, k)] = res
        return memo[(i, k)]



