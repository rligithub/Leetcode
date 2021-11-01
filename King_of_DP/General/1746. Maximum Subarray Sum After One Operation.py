class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        # 连续最大sum的subarry + 可以将其中一个数变成square
        # 连续最大sum的subarry--> prev_sum + nums[i]  vs. nums[i] --> see if we should restart or add up
        # 可以将其中一个数变成square --> operation vs. not_operation

        memo = {}

        self.dfs(nums, 0, True, memo)
        return max(memo.values())

    def dfs(self, nums, pos, can_square, memo):
        if (pos, can_square) in memo:
            return memo[(pos, can_square)]

        if pos == len(nums):
            return 0

        not_operation = max(self.dfs(nums, pos + 1, can_square, memo) + nums[pos], nums[pos])

        operation = 0
        if can_square:
            operation = max(self.dfs(nums, pos + 1, False, memo) + nums[pos] * nums[pos], nums[pos] * nums[pos])

        memo[(pos, can_square)] = max(operation, not_operation)
        return memo[(pos, can_square)]