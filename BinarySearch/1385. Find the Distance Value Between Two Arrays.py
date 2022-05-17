class Solution1:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr2.sort()

        # find if there is num in between minn and maxx in arr2 --> if yes, count ++ --> return n1 - count
        count = 0
        for i, num in enumerate(arr1):
            maxx = num + d
            minn = num - d

            left = bisect.bisect_left(arr2, minn)
            right = bisect.bisect_right(arr2, maxx)
            if left < right:
                count += 1

        return len(arr1) - count


class Solution2:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr2.sort()

        # find if there is num in between minn and maxx in arr2 --> if yes, count ++ --> return n1 - count
        count = 0
        for i, num in enumerate(arr1):
            maxx = num + d
            minn = num - d

            left = bisect.bisect_left(arr2, minn)
            right = bisect.bisect_left(arr2, maxx + 1)
            if left < right:
                count += 1

        return len(arr1) - count


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr2.sort()

        # find if there is num in between minn and maxx in arr2 --> if yes, count ++ --> return n1 - count
        count = 0
        for i, num in enumerate(arr1):
            maxx = num + d
            minn = num - d

            left = self.findFirstPosition(arr2, minn)
            right = self.findFirstPosition(arr2, maxx + 1)
            if left < right:
                count += 1

        return len(arr1) - count

    def findFirstPosition(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left


