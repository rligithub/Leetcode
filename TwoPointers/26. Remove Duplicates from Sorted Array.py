class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        while left < len(nums) and right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1

        return left + 1     # i is index