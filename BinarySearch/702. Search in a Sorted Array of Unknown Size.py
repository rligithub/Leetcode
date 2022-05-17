# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # 2x find target

        if reader.get(0) > target:
            return -1

        left = 0
        right = 1
        while reader.get(right) < target:
            left = right
            right = 2 * right

        while left <= right:
            mid = left + (right - left) // 2
            num = reader.get(mid)
            if num < target:
                left = mid + 1
            elif num == target:
                return mid
            else:
                right = mid - 1

        return -1
