class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # similar to copy book
        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2
            if self.timeSpend(piles, mid) <= h:  # find slowest speed --> find left boundary
                right = mid - 1
            else:
                left = mid + 1

        return left

    def timeSpend(self, nums, speed):

        time = 0

        for num in nums:
            if num % speed == 0:
                time += num // speed
            else:
                time += num // speed + 1
        return time


