class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        left, right = 1, max(nums)

        while left <= right:
            mid = left + (right - left) // 2
            summ = self.getSumm(nums, mid, threshold)

            if self.getSumm(nums, mid, threshold) <= threshold:  # qualified --> make mid smaller
                right = mid - 1
            else:
                left = mid + 1

        return left

    def getSumm(self, nums, divisor, threshold):
        res = 0
        for num in nums:
            res += math.ceil(num / divisor)
            if res > threshold:
                return res
        return res
