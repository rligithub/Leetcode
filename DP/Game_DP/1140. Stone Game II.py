class Solution:  # top down dp
    def stoneGameII(self, piles) -> int:
        # 给好几堆石头，每个人可以从左边拿 x 堆 (1<= X <= 2M），M从1开始。求先手最多拿多少个石头
        # memo --> # of stones the first player gets = remaining stones - # of stones the second player can get
        # use suffixsum
        n = len(piles)
        sufsum = [0] * n
        sufsum[0] = sum(piles)
        for i in range(1, n):
            sufsum[i] = sufsum[i - 1] - piles[i - 1]

        memo = {}
        return self.dfs(piles, sufsum, 0, 1, memo)

    def dfs(self, piles, sufsum, pos, M, memo):
        if (pos, M) in memo:
            return memo[(pos, M)]

        # over range
        if pos > len(piles) - 1:
            return 0
            # base case
        if pos >= len(piles) - 2 * M:
            return sufsum[pos]

        # MIN STONES THAT SECOND PLAYER CAN GET
        res = float('inf')
        for x in range(1, 2 * M + 1):
            res = min(res, self.dfs(piles, sufsum, pos + x, max(x, M), memo))

        # MAX STONES THAT FIRST PLAYER CAN GET = REMAINING - STONES THAT SECOND PLAYER GETS
        memo[(pos, M)] = sufsum[pos] - res
        return memo[(pos, M)]


piles = [2,7,9,4,4]
a = Solution()
print(a.stoneGameII(piles))