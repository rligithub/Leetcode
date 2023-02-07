class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minn = arrays[0][0]
        maxx = arrays[0][-1]
        res = 0

        for i, nums in enumerate(arrays[1:]):
            res = max(res, abs(maxx - nums[0]), abs(nums[-1] - minn))
            minn = min(minn, nums[0])
            maxx = max(maxx, nums[-1])

        return res




