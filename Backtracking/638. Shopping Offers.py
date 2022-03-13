class Solution1:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # backpack + 对于每个offer都可以选跟不选

        memo = {}
        return self.dfs(price, special, needs, memo)

    def dfs(self, price, special, needs, memo):
        if (tuple(needs)) in memo:
            return memo[tuple(needs)]

        cost = 0
        # CASE1 --> buy singely
        for i, p in enumerate(price):
            cost += needs[i] * p

        # CASE2 --> buy offer
        for offer in special:
            valid_offer = True
            for i in range(len(needs)):
                if offer[i] > needs[i]:
                    valid_offer = False
            if valid_offer:
                remain_needs = [0] * (len(needs))
                for i in range(len(needs)):
                    remain_needs[i] = needs[i] - offer[i]
                cost = min(cost, self.dfs(price, special, remain_needs, memo) + offer[-1])

        memo[tuple(needs)] = cost
        return memo[tuple(needs)]


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # backpack + 对于每个offer都可以选跟不选

        memo = {}
        return self.dfs(price, special, needs, memo)

    def dfs(self, price, special, needs, memo):
        if (tuple(needs)) in memo:
            return memo[tuple(needs)]

        cost = 0
        # CASE1 --> buy singely
        for i, p in enumerate(price):
            cost += needs[i] * p

        # CASE2 --> buy offer
        for offer in special:
            valid_offer = True
            remain_needs = [0] * (len(needs))

            for i in range(len(needs)):
                if offer[i] > needs[i]:
                    valid_offer = False
                remain_needs[i] = needs[i] - offer[i]

            if valid_offer:
                cost = min(cost, self.dfs(price, special, remain_needs, memo) + offer[-1])

        memo[tuple(needs)] = cost
        return memo[tuple(needs)]


class Solution2:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        # backpack + 对于每个offer都可以选跟不选

        memo = {}
        return self.dfs(price, special, needs, memo)

    def dfs(self, price, special, needs, memo):
        if (tuple(needs)) in memo:
            return memo[tuple(needs)]

        cost = 0
        # CASE1 --> buy singely
        for i, p in enumerate(price):
            cost += needs[i] * p

        # CASE2 --> buy offer
        for offer in special:
            valid_offer = True
            remain_needs = []

            for i in range(len(needs)):
                if offer[i] > needs[i]:
                    valid_offer = False
                remain_needs.append(needs[i] - offer[i])

            if valid_offer:
                cost = min(cost, self.dfs(price, special, remain_needs, memo) + offer[-1])

        memo[tuple(needs)] = cost
        return memo[tuple(needs)]