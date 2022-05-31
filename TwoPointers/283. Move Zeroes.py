class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # same direction --> keep the same order
        # left --> slower pointer --> swap each right to left.
        # right --> pointer to non-zero
        left, right = 0, 0

        while left < len(nums) and right < len(nums):
            if nums[right] == 0:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
        return nums
