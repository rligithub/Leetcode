class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        # search the duplicate num
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            count = 0

            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution:  # indexing sort
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
