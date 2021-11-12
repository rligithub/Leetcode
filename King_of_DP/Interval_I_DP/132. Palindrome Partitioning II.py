class Solution:
    def minCut(self, s: str) -> int:
        # 求最少切几刀使得 每一个substring都是palindrome --> 最少有几个palindrome
        # 区间DP --> for loop 长度 --> if substring is a palindrome

        # step1: 求是否是palindrome --> 左右比较 往中间移动
        dp = {}
        self.isPal(s, 0, len(s) - 1, dp)

        # step2: 求最少有几个palindrome --> 切几刀
        memo = {}
        return self.dfs(s, 0, dp, memo) - 1

    def isPal(self, s, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]

        # stop point --> 只剩一个char
        if i >= j:
            return True
        if s[i] != s[j]:
            return False
        if self.isPal(s, i + 1, j - 1, dp):
            dp[(i, j)] = True
            return True
        dp[(i, j)] = False
        return False

    def dfs(self, s, i, dp, memo):
        if i in memo:
            return memo[i]

        n = len(s)
        if i == n:
            return 0

        res = float('inf')
        # 比较不同长度下 最少的palindrome
        for j in range(i, n):
            if self.isPal(s, i, j, dp):
                res = min(res, self.dfs(s, j + 1, dp, memo) + 1)

        memo[i] = res
        return res










