class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # similar to 34 find first and last position of element in sorted array
        # find the left boundary + right boundary
        n = len(nums)

        left = self.binarySearch(nums, target)
        right = self.binarySearch(nums, target + 1)

        if right - left > n // 2:
            return True
        return False

    def binarySearch(self, nums, target):

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left