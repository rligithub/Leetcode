class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 背包问题 --> 每个数字用无限次， 顺序不同算一次 ==> 物品1中的for loop，物品2中的for loop，物品3中的for loop
        memo = {}
        return self.dfs(nums, target, memo)

    def dfs(self, nums, target, memo):
        if target in memo:
            return memo[target]

        if target == 0:
            return 1

        if target < 0:
            return 0

        res = 0
        # res是每一层的总和，每层reset
        for num in nums:
            res += self.dfs(nums, target - num, memo)

        memo[target] = res
        return memo[target]


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums or not target:
            return 0
        m = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1

        # i --> number of item
        # j --> size of backpack
        # dp[j] = dp[j - nums[0]] + dp[j - nums[1]] ... + dp[j - nums[m-1]]
        # 求dp[j] --> 回头看所有可能性，以dp[j]为行数，看每行的每一个的关系

        for j in range(1, target + 1):
            for i in range(m):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]
        return dp[-1]