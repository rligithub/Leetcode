class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # 找最长 index的跳跃个数 --> for loop每个点做dfs 找最长的个数

        res = 0
        memo = {}
        for i in range(len(nums)):
            res = max(res, self.dfs(nums, i, set(), memo))
        return res

    def dfs(self, nums, pos, visited, memo):
        if pos in memo:
            return memo[pos]

        if pos in visited:
            return len(visited)

        visited.add(pos)

        memo[pos] = self.dfs(nums, nums[pos], visited, memo)
        return memo[pos]

