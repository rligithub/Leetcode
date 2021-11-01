class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        # 给一个数组，求能不能分成两个subsets使得这两个subset的sum相等
        # 背包问题 --> 求数组的数能不能组成 target == sum // 2

        # dp[i][j] --> if the sum of items 0 ... i equals j

        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                # 如果前面的已经找到符合条件的，返回前面符合条件的解即可
                if j >= nums[i - 1]:
                    dp[i][j] |= dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        memo = {}
        return self.dfs(nums, 0, target, memo)

    def dfs(self, nums, pos, n, memo):
        if (pos, n) in memo:
            return memo[(pos, n)]

        if pos == len(nums) and n == 0:
            return True
        if pos == len(nums) and n > 0:
            return False

        not_pick = self.dfs(nums, pos + 1, n, memo)
        pick = False
        if n >= nums[pos]:
            pick = self.dfs(nums, pos + 1, n - nums[pos], memo)
        memo[(pos, n)] = not_pick or pick
        return memo[(pos, n)]