class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        if nums[left] > nums[right]:
            return left
        return right


class Solution: # template 2
    def findPeakElement(self, nums: List[int]) -> int:
        # find left boundary
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


class Solution: #template 3
    def findPeakElement(self, nums: List[int]) -> int:
        # find left boundary
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid

        if nums[left] < nums[right]:
            return right
        return left
