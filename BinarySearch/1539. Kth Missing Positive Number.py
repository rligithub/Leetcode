class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # 找出当前这个index有多少个missing_num， 比较一下k的值 ---> 返回 当前这个坐标 + k
        # 每一个下标处缺失的正整数的数量为a[loc]-loc-1

        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            NumOfMissing = arr[mid] - mid - 1
            if NumOfMissing < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k



