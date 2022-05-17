class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # find first position that greater than target --> left boundary

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return left


class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # find first position that greater than target --> left boundary

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return left
