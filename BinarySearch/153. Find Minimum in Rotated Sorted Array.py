class Solution:  # best + template 1 + compare [mid-1] to [mid]
    def findMin(self, nums: List[int]) -> int:
        # find minimum
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid - 1]:  # minimum val
                return nums[mid]

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid - 1

        return nums[left]


class Solution1:  # template 2
    def findMin(self, nums: List[int]) -> int:
        # need to compare neighbor

        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


class Solution2:  # template #1 + compare nums[0], search right
    def findMin(self, nums: List[int]) -> int:
        # need to compare neighbor

        left, right = 0, len(nums) - 1  # inclusive for [left, right]
        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:  # stop when left > right
            mid = left + (right - left) // 2
            if nums[mid] >= nums[0]:  # compare nums[0], search right
                left = mid + 1
            else:
                right = mid - 1

        return nums[left]


class Solution:  # template #1 + compare nums[-1], search left
    def findMin(self, nums: List[int]) -> int:
        # need to compare neighbor

        left, right = 0, len(nums) - 1  # inclusive for [left, right]
        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:  # stop when left > right
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:  # compare nums[-1], search left
                left = mid + 1
            else:
                right = mid - 1

        return nums[left]