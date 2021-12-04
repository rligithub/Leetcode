class Solution:
    def strangePrinter(self, s: str) -> int:
        # 类似moved box
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo)

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        # 不覆盖 打印
        res = self.dfs(s, i + 1, j, memo) + 1

        # 覆盖打印
        for k in range(i + 1, j + 1):
            if s[i] == s[k]:
                res = min(res, self.dfs(s, i+1, k - 1, memo) + self.dfs(s, k, j, memo))
        memo[(i, j)] = res
        return res



class Solution:  # slower!!! use #546 remove box methods
    def strangePrinter(self, s: str) -> int:
        memo = {}
        return self.dfs(s, 0, len(s) - 1, 0, memo)

    def dfs(self, s, i, j, k, memo):
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        if i > j:
            return 0

        while i < j and s[i] == s[i + 1]:
            i += 1
            k += 1

        # 一个一个打
        res = self.dfs(s, i + 1, j, 0, memo) + 1

        # 先打一排
        for m in range(i + 1, j + 1):
            if s[i] == s[m]:
                res = min(res, self.dfs(s, i + 1, m - 1, 0, memo) + self.dfs(s, m, j, k + 1, memo))
        memo[(i, j, k)] = res
        return res




