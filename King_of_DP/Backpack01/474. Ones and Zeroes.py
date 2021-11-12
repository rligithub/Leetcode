
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 求最多有几个subset 包含m个0和n个1
        table = []
        for str in strs:
            table.append([str.count('0'), str.count('1')])

        memo = {}
        return self.dfs(table, m, n, 0, memo)

    def dfs(self, table, zero, one, pos, memo):
        if (zero, one, pos) in memo:
            return memo[(zero, one, pos)]

        if zero < 0 or one < 0:
            return float('-inf')

        # base case
        if pos == len(table):
            return 0

        # base case
        if zero == 0 and one == 0:
            return 0

        pick = 0
        if table[pos][0] <= zero and table[pos][1] <= one:
            pick = self.dfs(table, zero - table[pos][0], one - table[pos][1], pos + 1, memo) + 1
        not_pick = self.dfs(table, zero, one, pos + 1, memo)

        memo[(zero, one, pos)] = max(pick, not_pick)
        return memo[(zero, one, pos)]


