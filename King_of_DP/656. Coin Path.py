class Solution1:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        memo = {}
        index = [-1] * n
        self.dfs(coins, maxjump, 0, index, memo)

        path = []
        # reconstruct
        cur = 0
        while cur != -1:
            path.append(cur + 1)
            cur = path[cur]
        return path

    def dfs(self, coins, pos, previndex, memo):
        if pos in memo:
            return memo[pos]

        if pos == len(coins):
            return -1

        if pos == len(coins) - 1 and coins[pos] != -1:
            memo[pos]


class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        if coins[-1] == -1:
            return []

        n = len(coins)
        # dp[i] --> the min cost from the end to index i
        dp = [float('inf')] * n
        # from the end to start --> initialization
        dp[-1] = coins[-1]

        index = [-1] * n

        for i in range(n - 2, -1, -1):
            if coins[i] == -1:
                continue
            for j in range(i + 1, min(i + maxJump, n - 1) + 1):
                if dp[j] == float('inf'):
                    continue
                if dp[j] + coins[i] < dp[i]:
                    dp[i] = dp[j] + coins[i]
                    index[i] = j

        if dp[0] == float('inf'):
            return []

        path = []

        cur = 0
        while cur != -1:
            path.append(cur + 1)
            cur = index[cur]

        return path








