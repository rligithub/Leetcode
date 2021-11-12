import collections


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # 找出每类产品的数量
        # 找出m个人的需要状态组合 --> 求出每种组合状态下所需要的 产品总个数
        # for loop 每类产品， 看是否此类产品能满足 其中的子状态 ===> 需要初始状态为 11111， 结束状态为00000
        # 如果产品数量 > 子状态需要的数量，并且 下一个状态 状态为其他的产品满足，return True

        count = collections.Counter(nums)
        prod = list(count.values())

        m, n = len(prod), len(quantity)
        state_table = [0] * (1 << n)

        for state in range(1 << n):
            for p in range(n):
                if state & (1 << p):
                    state_table[state] += quantity[p]

        memo = {}
        return self.dfs(prod, state_table, 0, (1 << n) - 1, memo)

    def dfs(self, prod, state_table, pos, state, memo):
        if (pos, state) in memo:
            return memo[(pos, state)]

        if state == 0:
            return True

        if pos == len(prod):
            return False

        subset = state
        while subset:
            if prod[pos] >= state_table[subset] and self.dfs(prod, state_table, pos + 1, state ^ subset, memo):
                memo[(pos, state)] = True
                return True
            subset = (subset - 1) & state

        memo[(pos, state)] = self.dfs(prod, state_table, pos + 1, state, memo)
        return memo[(pos, state)]








