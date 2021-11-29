class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # burst balloon
        # sort + [0] + [n] ---> 方便求每段长度
        cuts.sort()
        cuts = [0] + cuts + [n]
        memo = {}
        return self.dfs(cuts, 0, len(cuts) - 1, memo)

    def dfs(self, cuts, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # base case --> 相邻cut停下
        if i + 1 == j:
            return 0

        res = float('inf')
        # 注意之前加了padding
        for k in range(i + 1, j):
            res = min(res, self.dfs(cuts, i, k, memo) + self.dfs(cuts, k, j, memo) + (cuts[j] - cuts[i]))
        memo[(i, j)] = res
        return memo[(i, j)]

