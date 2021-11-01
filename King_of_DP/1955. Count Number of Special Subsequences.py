class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        # special --> 数组里包括 0， 1， 2 并且 数组顺序递增 0， 1， 2
        # 递增或相等 --> nums[i] >= nums[i-1]
        # 数组里包括 0， 1， 2

        memo = {}
        res = self.dfs(nums, 0, -1, memo)
        return res

    def dfs(self, nums, pos, prev, memo):
        if (pos, prev) in memo:
            return memo[(pos, prev)]

        if pos == len(nums):
            return prev == 2

        mod = 10 ** 9 + 7
        pick = 0
        not_pick = self.dfs(nums, pos + 1, prev, memo)
        if (nums[pos] == prev + 1) or (nums[pos] == prev):
            pick = self.dfs(nums, pos + 1, nums[pos], memo)

        memo[(pos, prev)] = (pick + not_pick) % mod
        return memo[(pos, prev)]



