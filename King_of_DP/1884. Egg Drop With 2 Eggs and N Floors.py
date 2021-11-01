class Solution1:
    def twoEggDrop(self, n: int) -> int:
        # 扔鸡蛋，给2个鸡蛋

        memo = {}
        return self.dfs(n, 2, memo)

    def dfs(self, n, k, memo):
        if (n, k) in memo:
            return memo[(n, k)]

        if k == 0:
            return 0

        if k == 1:
            return n

        if n <= 1:
            return n

        res = float('inf')
        for i in range(1, n):
            res = min(res, max(self.dfs(i - 1, k - 1, memo), self.dfs(n - i, k, memo)) + 1)

        memo[(n, k)] = res
        return memo[(n, k)]
