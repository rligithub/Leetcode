class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left = 0
        while left < len(nums) and nums[left] < 0:
            left += 1

        res = []
        right = left
        left = left - 1
        while left >= 0 and right < len(nums):
            if nums[left] ** 2 > nums[right] ** 2:
                res.append(nums[right] ** 2)
                right += 1
            elif nums[left] ** 2 < nums[right] ** 2:
                res.append(nums[left] ** 2)
                left -= 1
            else:
                res.append(nums[left] ** 2)
                res.append(nums[right] ** 2)
                left -= 1
                right += 1
        while left >= 0:
            res.append(nums[left] ** 2)
            left -= 1
        while right < len(nums):
            res.append(nums[right] ** 2)
            right += 1
        return res


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left, right = 0, len(nums) - 1
        res = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        return res[::-1]