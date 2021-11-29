class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        presum = [0]

        for stone in stones:
            presum.append(presum[-1] + stone)

        memo = {}
        return self.dfs(presum, 0, len(stones) - 1, memo)

    def dfs(self, presum, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        # CASE1： 如果Alice选择pick左边
        pickleft = presum[j + 1] - presum[i + 1] - self.dfs(presum, i + 1, j, memo)
        # CASE2： 如果Alice选择pick右边
        pickright = presum[j] - presum[i] - self.dfs(presum, i, j - 1, memo)

        memo[(i, j)] = max(pickleft, pickright)
        return memo[(i, j)]