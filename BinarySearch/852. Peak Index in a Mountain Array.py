class Solution:  # template 3
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # find peak

        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid

                # post processing
        if arr[left] > arr[right]:
            return left
        return right