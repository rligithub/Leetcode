class Solution1:  # binary search template 2
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # binary search diff --> check if there k diff less than it

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if self.getSmallerCount(nums, mid, k) < k:
                left = mid + 1
            else:
                right = mid
        return left

    def getSmallerCount(self, nums, target, k):
        count = 0
        i = 0
        for j, x in enumerate(nums):
            while x - nums[i] > target:
                i += 1
            count += j - i
        return count


class Solution2:  # binary search template 1
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # binary search diff --> check if there k diff less than it

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if self.getSmallerCount(nums, mid, k) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getSmallerCount(self, nums, target, k):
        count = 0
        i = 0
        for j, x in enumerate(nums):
            while x - nums[i] > target:
                i += 1
            count += j - i
        return count


class Solution1:  # binary search template 1
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # binary search diff --> check if there k diff less than it

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if self.getSmallerCount(nums, mid, k) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getSmallerCount(self, nums, target, k):
        count = 0
        for i, num in enumerate(nums):
            j = -1
            left, right = i + 1, len(nums) - 1  # find right boundary
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[i] + target:
                    right = mid - 1
                else:
                    j = mid
                    left = mid + 1
            print(j)
            if j != -1:
                count += j - i
        return count


class Solution:  # binary search template 1
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # binary search diff --> check if there k diff less than it

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if self.getSmallerCount(nums, mid, k) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getSmallerCount(self, nums, target, k):
        count = 0
        for i, num in enumerate(nums):
            j = bisect.bisect_right(nums, num + target, lo=i + 1)
            count += j - i - 1
        return count