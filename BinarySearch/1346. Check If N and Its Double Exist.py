class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # 检查是否存在一个n和n*2在数组里 --> for loop each num， find 2*num in array --> if exist and not itself(num zero), return True
        n = len(arr)
        arr.sort()

        for i in range(n):
            target = 2 * arr[i]
            pos = self.binarySearch(arr, target)
            if pos != -1 and pos != i:  # exclude num 0 --> 0*2 = 0
                return True

        return False

    def binarySearch(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1 