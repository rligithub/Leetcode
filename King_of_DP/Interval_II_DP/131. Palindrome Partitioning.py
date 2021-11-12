class Solution:
    def partition(self, s):
        # print every possible path that make each substring as palindrome
        dp = {}
        self.isPal(s, 0, len(s) - 1, dp)

        memo = {}
        res = []
        ans = self.dfs(s, 0, [], res, dp, memo)
        return ans

    def dfs(self, s, i, path, res, dp, memo):
        # if i in memo:
        #    return memo[i]

        if i >= len(s):
            res.append(path)
            return res

        for j in range(i, len(s)):
            if self.isPal(s, i, j, dp):
                self.dfs(s, j + 1, path + [s[i:j + 1]], res, dp, memo)

    def isPal(self, s, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]

        if i >= j:
            return True

        if s[i] != s[j]:
            return False

        if self.isPal(s, i + 1, j - 1, dp):
            dp[(i, j)] = True
            return True

        dp[(i, j)] = False
        return False


s = "aab"
a = Solution()
print(a.partition(s))

