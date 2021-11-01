class Solution1:  # bottom up dp
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

            # dp[i] -- > longest increasing subsequence from index 0 to index i

        n = len(nums)
        dp = [1] * n
        dp[0] = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


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



nums = [0,1,0,3,2,3]
a = Solution()
print(a.lengthOfLIS(nums))