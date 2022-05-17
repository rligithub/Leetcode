class Solution1:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # binary search to find first and last position of target, if any

        nums.sort()

        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        res = []
        if left != -1:
            i = left
            while i < right:
                res.append(i)
                i += 1
            return res
        return res


class Solution2:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # binary search to find first and last position of target, if any

        nums.sort()

        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_left(nums, target + 1)

        res = []
        if left != -1:
            i = left
            while i < right:
                res.append(i)
                i += 1
            return res
        return res


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # binary search to find first and last position of target, if any

        nums.sort()

        left = self.findFirstPosition(nums, target)
        right = self.findFirstPosition(nums, target + 1)

        res = []
        if left != -1:
            i = left
            while i < right:
                res.append(i)
                i += 1
            return res
        return res

    def findFirstPosition(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left