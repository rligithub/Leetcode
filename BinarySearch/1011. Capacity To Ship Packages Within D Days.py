class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search capacity --> compare days needed under the capacity, check it with days given
        # days --> either one day or len(weights) days
        # capacity --> max(weights) or sum(weights)

        left, right = max(weights), sum(weights)  # left 如果为min(weight)就没有意义了，只能通过一个

        while left <= right:
            mid = left + (right - left) // 2
            if self.getDays(weights, mid) < days:  # move right--> more days --> less capacity
                right = mid - 1
            else:
                left = mid + 1

        return left

    def getDays(self, weights, capacity):

        days = 0
        curWeight = 0
        for weight in weights:
            curWeight += weight
            if curWeight > capacity:
                days += 1
                curWeight = weight
        return days

