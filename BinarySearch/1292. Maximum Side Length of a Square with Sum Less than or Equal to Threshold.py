class Solution1:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # binary search for side length --> check if sum of square are <= threshold
        m, n = len(mat), len(mat[0])
        prefSum = [[0] * (n + 1) for _ in range((m + 1))]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefSum[i][j] = prefSum[i - 1][j] + prefSum[i][j - 1] + mat[i - 1][j - 1] - prefSum[i - 1][j - 1]

        left, right = 0, min(m, n)
        while left <= right:
            mid = left + (right - left) // 2
            if self.getSquareSum(prefSum, mid, threshold):  # find right boundary
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def getSquareSum(self, nums, size, k):
        m, n = len(nums), len(nums[0])
        for i in range(m - size):
            for j in range(n - size):
                summ = nums[i + size][j + size] - nums[i + size][j] - nums[i][j + size] + nums[i][j]
                if summ <= k:
                    return True
        return False


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # binary search for side length --> check if sum of square are <= threshold
        m, n = len(mat), len(mat[0])
        prefSum = [[0] * (n + 1) for _ in range((m + 1))]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefSum[i][j] = prefSum[i - 1][j] + prefSum[i][j - 1] + mat[i - 1][j - 1] - prefSum[i - 1][j - 1]

        res = 0
        left, right = 0, min(m, n)
        while left <= right:
            mid = left + (right - left) // 2
            if self.getSquareSum(prefSum, mid, threshold):  # find right boundary
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

    def getSquareSum(self, nums, size, k):
        m, n = len(nums), len(nums[0])
        for i in range(m - size):
            for j in range(n - size):
                summ = nums[i + size][j + size] - nums[i + size][j] - nums[i][j + size] + nums[i][j]
                if summ <= k:
                    return True
        return False