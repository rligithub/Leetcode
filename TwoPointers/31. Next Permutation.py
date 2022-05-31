class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 从右往左找，找出第一个 比后面小的数 作为left
        # 从右往左找，找出最小的比 left大的数，作为right
        # swap left 和 right
        # left之后的数 按大小排列
        # return
        n = len(nums)
        left, right = n - 2, n - 1

        while left >= 0 and nums[left] >= nums[left + 1]:
            left -= 1
        if left < 0:
            return nums.sort()
        for j in range(n - 1, -1, -1):
            if nums[j] > nums[left]:
                right = j
                break
        nums[left], nums[right] = nums[right], nums[left]
        nums[:] = nums[:left + 1] + sorted(nums[left + 1:])
