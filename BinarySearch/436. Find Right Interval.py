class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        res = []

        # sort
        nums = []
        for i, interval in enumerate(intervals):
            nums.append([interval[0], i])
        nums.sort()

        # binary search
        for start, end in intervals:
            pos = self.findNum(nums, end)
            if pos != -1:
                res.append(nums[pos][1])
            else:
                res.append(-1)
        return res

    def findNum(self, nums, target):
        res = -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid][0] == target:
                return mid
            elif nums[mid][0] > target:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
