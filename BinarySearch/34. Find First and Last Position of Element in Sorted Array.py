class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find first and last position --> search left boundary + search right boundary
        res = [-1, -1]

        # find first position
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                res[0] = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        # find last position
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                res[1] = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return res


class Solution2:  # template 1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find first and last position --> search left boundary + search right boundary
        res = [-1, -1]

        # find first position
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        if left < len(nums) and nums[left] == target:
            res[0] = left

        # find last position
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if 0 <= right and nums[right] == target:
            res[1] = right
        return res


class Solution3:  # template 2
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find left boundary of target and left boundary of target + 1
        left = self.binarySearch(nums, target)
        right = self.binarySearch(nums, target + 1) - 1

        if left < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]

    def binarySearch(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return left


class Solution:  # template 2
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find left boundary of target and left boundary of target + 1
        left = self.binarySearch(nums, target)
        right = self.binarySearch(nums, target + 1) - 1

        if left < len(nums) and nums[left] == target:
            return [left, right]
        return [-1, -1]

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left







