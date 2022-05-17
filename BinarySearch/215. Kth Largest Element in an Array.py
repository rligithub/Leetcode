class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # binary search num --> check if there is k num greater or equal to it

        left, right = min(nums), max(nums)

        while left <= right:
            mid = left + (right - left) // 2
            if self.getGreaterCount(nums, mid, k) >= k:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

    def getGreaterCount(self, nums, target, k):
        count = 0
        for num in nums:
            if num >= target:
                count += 1
            if count >= k:
                return count
        return count