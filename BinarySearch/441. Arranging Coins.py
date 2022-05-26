class Solution1:  # template 2
    def arrangeCoins(self, n: int) -> int:
        # find last position
        left, right = 0, n + 1

        while left < right:
            mid = left + (right - left) // 2
            summ = mid * (mid + 1) / 2
            if summ > n:
                right = mid
            else:
                left = mid + 1
        return left - 1


class Solution:  # template 3
    def arrangeCoins(self, n: int) -> int:
        # find last position
        left, right = 0, n

        while left <= right:
            mid = left + (right - left) // 2
            summ = mid * (mid + 1) / 2
            if summ > n:
                right = mid - 1
            else:
                left = mid + 1
        if left > 0:
            return left - 1
        return -1
