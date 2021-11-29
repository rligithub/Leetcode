class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        return self.dfs(nums1, nums2, 0, 0, memo)

    def dfs(self, nums1, nums2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(nums1) or j == len(nums2):
            return float('-inf')

        # take cur with prev vs take cur only
        take = max(nums1[i] * nums2[j], self.dfs(nums1, nums2, i + 1, j + 1, memo) + nums1[i] * nums2[j])
        # not take nums1 vs not take nums2
        not_take = max(self.dfs(nums1, nums2, i + 1, j, memo), self.dfs(nums1, nums2, i, j + 1, memo))

        memo[(i, j)] = max(take, not_take)
        return memo[(i, j)]

