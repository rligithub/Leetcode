class Solution1:
    def specialArray(self, nums: List[int]) -> int:
        # binary search to find x
        n = len(nums)
        nums.sort()

        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            less_than = self.getNumOfGreaterOrEqual(nums, mid)
            count = n - less_than
            if count == mid:
                return mid
            elif count > mid:  # more count, mid is too small --> left = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def getNumOfGreaterOrEqual(self, nums, target):  # find first position

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # binary search to find x
        n = len(nums)
        nums.sort()

        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            count = self.getNumOfGreaterOrEqual(nums, mid)
            if count == mid:
                return mid
            elif count > mid:  # more count, mid is too small --> left = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def getNumOfGreaterOrEqual(self, nums, target):  # find first position
        count = 0
        for num in nums:
            if num >= target:
                count += 1
        return count