class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            nums = [0] * m
            for right in range(left, n):
                for i in range(m):
                    nums[i] += matrix[i][right]
                res = max(res, self.kadane(nums, k))
        return res


    def kadane(self, nums, k):
        curSum, maxSum = 0, float('-inf')
        dp = [0]
        for i, num in enumerate(nums):
            curSum += num
            idx = bisect.bisect_left(dp, curSum - k)
            if idx != len(dp):
                maxSum = max(maxSum, curSum - dp[idx])
            bisect.insort(dp, curSum)
        return maxSum