class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        firstDiff = {0 : -1}
        diff, res = 0, 0
        for i in range(len(nums1)):
            diff += nums1[i] - nums2[i]
            if diff not in firstDiff:
                firstDiff[diff] = i
            else:
                res = max(res, i - firstDiff[diff])
        return res  