class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 背包 --> 把石头分为两堆，使得差值最小
        memo = {}
        return self.dfs(stones, 0, 0, 0, memo)

    def dfs(self, stones, sum1, sum2, pos, memo):
        if (sum1, sum2, pos) in memo:
            return memo[(sum1, sum2, pos)]

        if pos > len(stones) - 1:
            return abs(sum1 - sum2)

        left = self.dfs(stones, sum1 + stones[pos], sum2, pos + 1, memo)
        right = self.dfs(stones, sum1, sum2 + stones[pos], pos + 1, memo)

        memo[(sum1, sum2, pos)] = min(left, right)
        return memo[(sum1, sum2, pos)]

