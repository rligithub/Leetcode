class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 求最大sum 且能够被3整除

        memo = {}
        return self.dfs(nums, 0, 0, memo)

    def dfs(self, nums, pos, reminder, memo):
        if (pos, reminder) in memo:
            return memo[(pos, reminder)]

        if pos == len(nums):
            if reminder == 0:
                return 0
            else:
                return float('-inf')

        not_pick = self.dfs(nums, pos + 1, reminder, memo)
        n_reminder = (reminder + nums[pos]) % 3
        pick = self.dfs(nums, pos + 1, n_reminder, memo) + nums[pos]

        memo[(pos, reminder)] = max(pick, not_pick)
        return memo[(pos, reminder)]
