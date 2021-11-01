class Solution:  # top down dp
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # 两个选手，每次从末端拿一个数，看谁的积分多谁赢
        # memo --> 存的是两个人的当前总积分差
        memo = {}
        return self.dfs(nums, 0, len(nums) - 1, memo) >= 0

    def dfs(self, nums, l, r, memo):
        if (l, r) in memo:
            return memo[(l, r)]

        if l > r:
            return 0

        # PICK LEFT vs PICK RIGHT
        memo[(l, r)] = max(nums[l] - self.dfs(nums, l + 1, r, memo), nums[r] - self.dfs(nums, l, r - 1, memo))
        return memo[(l, r)]