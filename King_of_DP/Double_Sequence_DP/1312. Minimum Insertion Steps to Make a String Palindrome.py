class Solution1:
    def minInsertions(self, s: str) -> int:
        # 区间dp --> 求有几个不同的char
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        if s[i] == s[j]:
            res = self.dfs(s, i + 1, j - 1, memo)
        else:
            res = min(self.dfs(s, i + 1, j, memo), self.dfs(s, i, j - 1, memo)) + 1

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution2:
    def minInsertions(self, s: str) -> int:
        # 双序列dp --> 求LIC 然后求diff
        memo = {}
        LIC = self.dfs(s, s[::-1], 0, 0, memo)
        return len(s) - LIC

    def dfs(self, s, t, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s) or j == len(s):
            return 0

        if s[i] == t[j]:
            res = self.dfs(s, t, i + 1, j + 1, memo) + 1
        else:
            res = max(self.dfs(s, t, i + 1, j, memo), self.dfs(s, t, i, j + 1, memo))

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution:
    def minInsertions(self, s: str) -> int:
        # 双序列dp --> 求最短公共祖先Shortest-Common-Supersequence，求diff
        memo = {}
        SCS = self.dfs(s, s[::-1], 0, 0, memo)
        print(SCS)
        return SCS - len(s)

    def dfs(self, s, t, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # ** BASE CASE ** differ from LIC
        if i == len(s):
            return len(t) - j
        if j == len(t):
            return len(s) - i

        if s[i] == t[j]:
            res = self.dfs(s, t, i + 1, j + 1, memo) + 1
        else:
            res = min(self.dfs(s, t, i + 1, j, memo), self.dfs(s, t, i, j + 1, memo)) + 1

        memo[(i, j)] = res
        return memo[(i, j)]
