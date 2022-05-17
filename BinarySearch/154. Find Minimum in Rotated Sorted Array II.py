class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find minimum --> with duplicated value
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid - 1]:  # minimum val
                return nums[mid]

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid - 1
            else:
                right -= 1  # de-duplicated

        return nums[left]



