class Solution:
    def knightDialer(self, n: int) -> int:
        # 预处理：把每个数字键能走到的距离 存起来
        table = {1: [6, 8],
                 2: [7, 9],
                 3: [4, 8],
                 4: [0, 3, 9],
                 5: [],
                 6: [0, 1, 7],
                 7: [2, 6],
                 8: [1, 3],
                 9: [2, 4],
                 0: [4, 6]}
        memo = {}
        res = 0
        mod = 10 ** 9 + 7
        for i in range(10):
            res += self.dfs(n - 1, i, table, memo)
        return res % mod

    def dfs(self, n, neighbor, table, memo):
        if (n, neighbor) in memo:
            return memo[(n, neighbor)]

        if n == 0:
            return 1
        mod = 10 ** 9 + 7
        res = 0
        for nei in table[neighbor]:
            res += self.dfs(n - 1, nei, table, memo)

        memo[(n, neighbor)] = res % mod
        return memo[(n, neighbor)]

