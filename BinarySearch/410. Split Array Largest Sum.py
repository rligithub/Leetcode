class Solution:  # binary search
    def splitArray(self, nums: List[int], m: int) -> int:
        # binary search max summ --> see if it can be split to m array

        left, right = max(nums), sum(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if self.getCount(nums, mid) > m:  # reduce splits, increase mid
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getCount(self, nums, k):
        summ = 0
        count = 1
        for num in nums:
            if summ + num > k:
                count += 1
                summ = num
            else:
                summ += num

        return count



