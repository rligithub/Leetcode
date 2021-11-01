import collections


class Solution:
    def numWays(self, words: List[str], target: str) -> int:

        m, n = len(words), len(words[0])

        table = collections.defaultdict(collections.Counter)

        for i in range(m):
            for j in range(n):
                table[j][words[i][j]] += 1

        memo = {}
        return self.dfs(table, target, 0, 0, memo)

    def dfs(self, table, target, pos, k, memo):
        if (pos, k) in memo:
            return memo[(pos, k)]

        if pos == len(target):
            return 1

        if k == len(table):
            return 0

        mod = 10 ** 9 + 7

        pick = 0
        # pick
        if table[k][target[pos]]:
            pick = self.dfs(table, target, pos + 1, k + 1, memo) * table[k][target[pos]]

        # not pick
        not_pick = self.dfs(table, target, pos, k + 1, memo)

        memo[(pos, k)] = (not_pick + pick) % mod
        return memo[(pos, k)]