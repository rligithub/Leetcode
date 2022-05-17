class Solution:
    def arrangeCoins(self, n: int) -> int:
        # find last position
        left, right = 0, n

        while left <= right:
            mid = left + (right - left) // 2
            summ = mid * (mid + 1) / 2
            if summ == n:
                return mid
            elif summ > n:
                right = mid - 1
            else:
                left = mid + 1
        return right 