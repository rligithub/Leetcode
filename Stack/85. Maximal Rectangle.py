class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [0] * n
        res = 0
        for row in matrix:
            for j in range(n):
                if row[j] == "0":
                    dp[j] = 0
                else:
                    dp[j] += 1
            res = max(res, self.findMaxRectangle(dp))
        return res

    def findMaxRectangle(self, nums):
        stack = [-1]
        nums.append(0)
        res = 0

        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                h = nums[stack.pop()]
                w = i - 1 - stack[-1]
                res = max(res, h * w)
            stack.append(i)

        return res 