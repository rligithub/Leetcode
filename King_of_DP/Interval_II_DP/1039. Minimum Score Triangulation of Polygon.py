class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # 类似题：burst balloon

        memo = {}
        return self.dfs(values, 0, len(values) - 1, memo)

    def dfs(self, values, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        # 三个点才能组成三角形
        if i + 2 > j:
            return 0

            # i, j, k 的值不止一次被用到，可以在其他三角形中用到
        res = float('inf')
        for k in range(i + 1, j):
            res = min(res,
                      self.dfs(values, i, k, memo) + self.dfs(values, k, j, memo) + values[i] * values[k] * values[j])

        memo[(i, j)] = res
        return res