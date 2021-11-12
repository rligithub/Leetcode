class Solution1:  # TLE
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        return self.dfs(nums, -1, 0, memo)

    def dfs(self, nums, prev, pos, memo):
        if (prev, pos) in memo:
            return memo[(prev, pos)]

        if pos >= len(nums):
            return 0

        take, not_take = 0, 0
        if prev < 0 or nums[prev] < nums[pos]:
            take = self.dfs(nums, pos, pos + 1, memo) + 1
        not_take = self.dfs(nums, prev, pos + 1, memo)

        memo[(prev, pos)] = max(take, not_take)
        return memo[(prev, pos)]


class Solution:  # top down dp
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        res = 0
        for i in range(len(nums)):
            res = max(res, self.dfs(nums, i, memo) + 1)
        return res

    def dfs(self, nums, pos, memo):
        if pos in memo:
            return memo[pos]

        # over range
        if pos == len(nums):
            return 0

        res = 0
        for i in range(pos, len(nums)):
            if nums[i] > nums[pos]:
                res = max(res, self.dfs(nums, i, memo) + 1)

        memo[pos] = res
        return memo[pos]