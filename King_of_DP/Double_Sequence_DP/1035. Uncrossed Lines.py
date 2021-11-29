class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        return self.dfs(nums1, nums2, 0, 0, memo)

    def dfs(self, nums1, nums2, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(nums1) or j == len(nums2):
            return 0

        if nums1[i] == nums2[j]:
            res = self.dfs(nums1, nums2, i + 1, j + 1, memo) + 1
        else:
            res = max(self.dfs(nums1, nums2, i + 1, j, memo), self.dfs(nums1, nums2, i, j + 1, memo))

        memo[(i, j)] = res
        return memo[(i, j)]
