class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        # find first position
        left, right = 0, len(arr) - 1

        res = -1
        while left <= right:
            mid = left + (right - left) // 2
            if mid == arr[mid]:
                res = mid
                right = mid - 1
            elif mid > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return res 