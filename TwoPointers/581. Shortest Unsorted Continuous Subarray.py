class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return 0

        copy = sorted(nums)
        n = len(nums)

        left, right = 0, len(nums) - 1

        while left < len(nums) and nums[left] == copy[left]:
            left += 1

        if left == len(nums):
            return 0

        while right >= 0 and nums[right] == copy[right]:
            right -= 1

        return right - left + 1


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        test = sorted(nums)
        n = len(nums)

        left, right = -1, -1

        for i in range(n):
            if nums[i] != test[i]:
                left = i
                break

        for i in range(n - 1, -1, -1):
            if nums[i] != test[i]:
                right = i
                break

        if left == -1 and right == -1:
            return 0

        return right - left + 1