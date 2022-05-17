class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        # binary search find mini val --> check if change all int large than value to value, summ of array is closest to target --> template 2 to find clostest ans

        left, right = 0, max(arr)  # not neccesarilly a number from arr

        while left < right:
            mid = left + (right - left) // 2
            summ = self.getSum(arr, mid)
            if summ >= target:  # large summ --> need to be smaller to get small summ
                right = mid
            else:
                left = mid + 1
        if abs(self.getSum(arr, left) - target) < abs(self.getSum(arr, left - 1) - target):
            return left
        return left - 1

    def getSum(self, arr, k):
        res = 0
        for num in arr:
            if num > k:
                res += k
            else:
                res += num
        return res

