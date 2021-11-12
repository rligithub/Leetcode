import collections


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # 每个人可以选几种帽子 --> 换一个思路，要不要把这个帽子分配给这个人 （独特性）
        # stop point --> 如果每个人都有帽子
        # 求 solution #

        # n --> num of people
        n = len(hats)

        hat2p = collections.defaultdict(list)
        for p, hs in enumerate(hats):
            for h in hs:
                hat2p[h].append(p)

                # stop point --> 如果每个人都有帽子
        full_mask = (1 << n) - 1
        memo = {}
        return self.dfs(full_mask, 0, 1, hat2p, memo)

    def dfs(self, full_mask, state, pos, table, memo):
        if (state, pos) in memo:
            return memo[(state, pos)]

        mod = 10 ** 9 + 7

        # stop point -- > mask代表目前为止大家是否有帽子
        if state == full_mask:
            return 1

            # over range --> pos代表第几个帽子
        if pos > 40:
            return 0

            # 这个帽子没人想戴 --> 都不给
        res = self.dfs(full_mask, state, pos + 1, table, memo)
        # 这个帽子有人想戴 --> 给谁?

        for i in table[pos]:
            # 检查p这个人 是否已经有帽子了
            if (state & (1 << i)) == 0:
                # 给不同人的结果 是累积相加的
                res = res + self.dfs(full_mask, state | (1 << i), pos + 1, table, memo)

        memo[(state, pos)] = res % mod
        return memo[(state, pos)]



