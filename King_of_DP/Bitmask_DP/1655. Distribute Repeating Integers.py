import collections


class Solution1: # subset solution -- 11111 --> 0
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # only care about count of same products, not product ID
        # preprocessing to get the count of each products
        # for loop each products to see if it meet the demand for each state(mask)
        # if yes, turn of 11111 ---> 0000

        count = collections.Counter(nums)
        product = list(count.values())

        n = len(quantity)
        demand = [0] * (1 << n)

        for state in range(1 << n):
            for p in range(n):
                if state & (1 << p):
                    demand[state] += quantity[p]

        memo = {}
        return self.dfs(demand, product, (1 << n) - 1, 0, memo)

    def dfs(self, demand, product, state, pos, memo):
        if (state, pos) in memo:
            return memo[(state, pos)]

        if state == 0:
            return True

        if pos == len(product):
            return False

        # pick
        substate = state
        while substate:
            if product[pos] >= demand[substate] and self.dfs(demand, product, state ^ substate, pos + 1, memo):
                memo[(state, pos)] = True
                return True
            substate = (substate - 1) & state

        # not pick
        if self.dfs(demand, product, state, pos + 1, memo):
            memo[(state, pos)] = True
            return True

        memo[(state, pos)] = False
        return False


import collections


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # only care about count of same products, not product ID
        # preprocessing to get the count of each products
        # for loop each products to see if it meet the demand for each state(mask)
        # if yes, turn of 11111 ---> 0000

        count = collections.Counter(nums)
        product = list(count.values())

        n = len(quantity)
        demand = [0] * (1 << n)

        for state in range(1 << n):
            for p in range(n):
                if state & (1 << p):
                    demand[state] += quantity[p]

        memo = {}
        return self.dfs(demand, product, (1 << n) - 1, 0, memo)

    def dfs(self, demand, product, state, pos, memo):
        if (state, pos) in memo:
            return memo[(state, pos)]

        if state == 0:
            return True

        if pos == len(product):
            return False

        substate = state
        while substate:
            if product[pos] >= demand[substate] and self.dfs(demand, product, state ^ substate, pos + 1, memo):
                memo[(state, pos)] = True
                return True
            substate = (substate - 1) & state

        memo[(state, pos)] = self.dfs(demand, product, state, pos + 1, memo)
        return memo[(state, pos)]


class Solution3: # general solution -- 0 --> 11111
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        count = collections.Counter(nums)
        product = list(count.values())

        n, m = len(product), len(quantity)
        fullmask = (1 << m) - 1

        memo = {}

        return self.dfs(product, quantity, fullmask, 0, 0, memo)

    def dfs(self, product, quantity, fullmask, state, pos, memo):
        if (state, pos) in memo:
            return memo[(state, pos)]

        n, m = len(product), len(quantity)
        if state == fullmask:
            return True
        if pos == n:
            return False

            # check each state to find next state --> nextstate must have more demand than state, find the pos of new demand, calculate cost. compare if product meet the demand needs.
        for nxtState in range(1 << m):
            if nxtState & state != state:
                continue
            cost = 0
            for j in range(m):
                if state & (1 << j) == 0 and nxtState & (1 << j):
                    cost += quantity[j]
            if cost <= product[pos] and self.dfs(product, quantity, fullmask, nxtState, pos + 1, memo):
                memo[(state, pos)] = True
                return True

        memo[(state, pos)] = self.dfs(product, quantity, fullmask, state, pos + 1, memo)
        return memo[(state, pos)]



