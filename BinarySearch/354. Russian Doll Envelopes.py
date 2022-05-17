class Solution1:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # similar to #300 longest increasing subsequence

        # step1: sort envelops by x from small to large, y from large to small --> required x and y need to be greater than previous
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # step2: find pos that greater than/equal to target
        res = []
        for item in envelopes:
            height = item[1]
            pos = self.findNum(res, height)
            if pos < len(res):
                res[pos] = height
            else:
                res.append(height)
        return len(res)

    def findNum(self, nums, target):

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes or not envelopes[0]:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        res = []
        for envelope in envelopes:
            height = envelope[1]
            if len(res) == 0 or height > res[-1]:
                res.append(height)
            else:
                pos = bisect.bisect_left(res, height)
                res[pos] = height
        return len(res)