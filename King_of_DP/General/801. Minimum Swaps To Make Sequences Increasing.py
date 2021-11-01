class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # 可以交换 nums1和nums2 同一个index位置的数，使得nums1和nums2是递增的数，求min swap
        # if nums1 > prev1 and nums2 > prev2 --> no change
        # if nums1 > prev2 and nums2 > prev1 --> can change
        # we don't know if prev is swapped or not, add variable "prev"

        memo = {}
        return self.dfs(nums1, nums2, 0, -1, -1, memo)

    def dfs(self, nums1, nums2, pos, prev1, prev2, memo):
        if (pos, prev1, prev2) in memo:
            return memo[(pos, prev1, prev2)]

        if pos >= len(nums1):
            return 0

            # not_change vs change
        change = float('inf')
        if nums2[pos] > prev1 and nums1[pos] > prev2:
            change = self.dfs(nums1, nums2, pos + 1, nums2[pos], nums1[pos], memo) + 1

        not_change = float('inf')
        if nums1[pos] > prev1 and nums2[pos] > prev2:
            not_change = self.dfs(nums1, nums2, pos + 1, nums1[pos], nums2[pos], memo)

        memo[(pos, prev1, prev2)] = min(not_change, change)
        return memo[(pos, prev1, prev2)]



