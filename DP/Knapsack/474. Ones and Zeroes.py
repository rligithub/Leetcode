class Solution:  # top down dp
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 背包问题 --> 求需要几个items 组成 m个0 和 n个1

        # 求解每个substring里有几个 1 和 0
        table = []
        for str in strs:
            table.append([str.count('0'), str.count('1')])

        memo = {}
        return self.dfs(table, m, n, 0, memo)

    def dfs(self, table, m, n, pos, memo):
        if (m, n, pos) in memo:
            return memo[(m, n, pos)]

        if m == 0 and n == 0:
            return 0
        if pos == len(table):
            return 0

        pick = 0
        if m - table[pos][0] >= 0 and n - table[pos][1] >= 0:
            pick = self.dfs(table, m - table[pos][0], n - table[pos][1], pos + 1, memo) + 1
        not_pick = self.dfs(table, m, n, pos + 1, memo)

        memo[(m, n, pos)] = max(pick, not_pick)
        return memo[(m, n, pos)]