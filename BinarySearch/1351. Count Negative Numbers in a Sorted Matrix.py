class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # note that the order is deascending
        res = 0
        for row in grid:
            if row[-1] >= 0:
                continue
            idx = self.binarySearch(row, -1)
            res += len(row) - idx
        return res

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
        return left
