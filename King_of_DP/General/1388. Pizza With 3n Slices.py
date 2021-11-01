'''
Initial ideas:
- can't pick any of adjancent pizzas (Alice pick your left, Bob pick your right) ==> house robber
- circled ==> nums[1:] vs nums[:-1]
- base case: at most can pick (n // 3)

'''


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        k = n // 3
        return max(self.dfs(slices[:-1], 0, k, {}), self.dfs(slices[1:], 0, k, {}))

    def dfs(self, slices, pos, k, memo):
        if (pos, k) in memo:
            return memo[(pos, k)]

        if k == 0:
            return 0

        if pos >= len(slices):
            return 0

        not_pick = self.dfs(slices, pos + 1, k, memo)
        pick = self.dfs(slices, pos + 2, k - 1, memo) + slices[pos]

        memo[(pos, k)] = max(not_pick, pick)
        return memo[(pos, k)]
