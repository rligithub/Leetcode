class Solution:  # bottom up dp
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 求有几个最长递增子序列
        # dp求最长子递增序列，用count更新当前i为止有几个同样长度的递增子序列
        # 求出max(dp)，如果dp == max(dp)，求累积的count
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        count = [1] * n

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # update dp[i] and count[i] --> max(dp[i], dp[j] + 1)
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]

        res = 0
        maxLen = max(dp)
        for i in range(n):
            if dp[i] == maxLen:
                res += count[i]
        return res



