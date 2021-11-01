class Solution:  # top down dp
    def stoneGame(self, piles: List[int]) -> bool:
        # 每个人从两端拿一堆石头，拿完为止。看谁的石头多
        # memo存的是两个人当前积分差
        memo = {}
        return self.dfs(piles, 0, len(piles) - 1, memo) > 0

    def dfs(self, piles, l, r, memo):
        if (l, r) in memo:
            return memo[(l, r)]

        if l > r:
            return 0

        # PICK LEFT vs PICK RIGHT
        memo[(l, r)] = max(piles[l] - self.dfs(piles, l + 1, r, memo), piles[r] - self.dfs(piles, l, r - 1, memo))

        return memo[(l, r)]
