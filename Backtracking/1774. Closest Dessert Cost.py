class Solution:  # super fast
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # combination 1 from base + combination x from topping(each topping max 2) + to get min(abs(summ - target))
        self.minn = float('inf')
        self.res = 0
        for base in baseCosts:
            self.dfs(toppingCosts, target, 0, base)
        return self.res

    def dfs(self, toppingCosts, target, i, summ):  # i is for current topping cst is cost till now
        diff = abs(target - summ)

        if diff > self.minn and summ > target:
            return

        if diff == self.minn:
            self.res = min(self.res, summ)
        if diff < self.minn:
            self.minn = diff
            self.res = summ

        if i >= len(toppingCosts):
            return

        self.dfs(toppingCosts, target, i + 1, summ)
        self.dfs(toppingCosts, target, i + 1, summ + toppingCosts[i])
        self.dfs(toppingCosts, target, i + 1, summ + toppingCosts[i] * 2)


class Solution1:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        n = len(toppingCosts)
        toppings = [0]

        def dfs(i, total):
            if i >= n:
                toppings.append(total)
                return

            dfs(i + 1, total)
            dfs(i + 1, total + toppingCosts[i])
            dfs(i + 1, total + 2 * toppingCosts[i])

        dfs(0, 0)
        res = []
        for topping in toppings:
            for base in baseCosts:
                summ = base + topping
                res.append([abs(target - summ), summ])

        res = sorted(res)
        # print(res)
        return res[0][1]
