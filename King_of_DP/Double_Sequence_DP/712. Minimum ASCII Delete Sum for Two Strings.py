class Solution1:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # 转换成ASCII value ---> ord('a')
        memo = {}
        return self.dfs(s1, s2, 0, 0, memo)

    def dfs(self, s1, s2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        res = 0
        if i == len(s1):
            for x in range(j, len(s2)):
                res += ord(s2[x])
            return res

        if j == len(s2):
            for y in range(i, len(s1)):
                res += ord(s1[y])
            return res

        if s1[i] == s2[j]:
            res = self.dfs(s1, s2, i + 1, j + 1, memo)
        else:
            res = min(self.dfs(s1, s2, i + 1, j, memo) + ord(s1[i]), self.dfs(s1, s2, i, j + 1, memo) + ord(s2[j]))

        memo[(i, j)] = res
        return memo[(i, j)]


class Solution:  # slower
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        return self.dfs(s1, s2, 0, 0, memo)

    def dfs(self, s1, s2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s1) or j == len(s2):
            return sum([ord(i) for i in s1[i:]]) or sum([ord(i) for i in s2[j:]])

        if s1[i] == s2[j]:
            res = self.dfs(s1, s2, i + 1, j + 1, memo)
        else:
            res = min(self.dfs(s1, s2, i + 1, j, memo) + ord(s1[i]), self.dfs(s1, s2, i, j + 1, memo) + ord(s2[j]))

        memo[(i, j)] = res
        return memo[(i, j)]
