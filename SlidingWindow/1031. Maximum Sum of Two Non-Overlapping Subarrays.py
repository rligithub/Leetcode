class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        memo = {}
        return self.dfs(nums, firstLen, secondLen, 0, memo)

    def dfs(self, nums, x, y, i, memo):
        if (x, y, i) in memo:
            return memo[(x, y, i)]

        if i >= len(nums):
            return 0

        if x == 0 and y == 0:
            return 0

        not_pick = self.dfs(nums, x, y, i + 1, memo)
        if x == 0:
            pick = self.dfs(nums, x, 0, i + y, memo) + sum(nums[i:i + y])
            res = max(not_pick, pick)
        elif y == 0:
            pick = self.dfs(nums, 0, y, i + x, memo) + sum(nums[i:i + x])
            res = max(not_pick, pick)
        else:
            pick_x = self.dfs(nums, 0, y, i + x, memo) + sum(nums[i:i + x])
            pick_y = self.dfs(nums, x, 0, i + y, memo) + sum(nums[i:i + y])
            res = max(not_pick, pick_x, pick_y)

        memo[(x, y, i)] = res
        return res 