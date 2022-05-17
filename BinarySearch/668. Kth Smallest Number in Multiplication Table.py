class Solution1:  # TLE
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # ascending order for row, ascending order for col
        # guess the num --> check if there is k num less than it

        left, right = 1, m * n
        while left <= right:
            mid = left + (right - left) // 2
            if self.getNumOfSmaller(m, n, k, mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getNumOfSmaller(self, m, n, k, target):
        # use binary search to find how many num is less than target --> find right boundary
        count = 0
        for i in range(1, m + 1):
            left, right = 1, n
            while left <= right:
                mid = left + (right - left) // 2
                if i * mid <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            count += right
            if count > k:
                break
        return count


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # ascending order for row, ascending order for col
        # guess the num --> check if there is k num less than it

        left, right = 1, m * n
        while left <= right:
            mid = left + (right - left) // 2
            if self.getNumOfSmaller(m, n, k, mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getNumOfSmaller(self, m, n, k, target):
        count = 0
        for i in range(1, m + 1):
            count += min(target // i, n)  # faster!
            if target // i == 0 or count > k:
                break  # no need to do further count
        return count