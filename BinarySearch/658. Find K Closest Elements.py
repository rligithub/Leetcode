class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 找左边界 --> 确定打印的区间为【left，left+k】 打印k个

        left, right = 0, len(arr) - 1 - k

        while left <= right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid - 1

        return arr[left:left + k]