"""
test
"""

def test():
    print('tony')

test()

class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        while i < j and s[i] == s[i+1]:
            i += 1

        # 一个一个打
        res = self.dfs(s, i + 1, j, memo) + 1

        # 先打一排
        for k in range(i + 1, j + 1):
            if s[i] == s[k]:
                res = max(res, self.dfs(s, i + 1, k - 1, memo) + self.dfs(s, k, j, memo))

        memo[(i, j)] = res
        return res

a = Solution()
b = "aba"
print(a.strangePrinter(b))