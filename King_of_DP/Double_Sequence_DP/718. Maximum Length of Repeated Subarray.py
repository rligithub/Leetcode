class Solution1:  # bottom up
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 求共同最长subarry --> 不是subsequence
        m, n = len(nums1), len(nums2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
        return res


class Solution:  # top down # TLE
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 求共同最长subarry
        memo = {}
        return self.dfs(nums1, nums2, 0, 0, 0, memo)

    def dfs(self, nums1, nums2, i, j, cnt, memo):
        if (i, j, cnt) in memo:
            return memo[(i, j, cnt)]

        if i == len(nums1) or j == len(nums2):
            return cnt

        cnt1 = cnt
        if nums1[i] == nums2[j]:
            cnt1 = self.dfs(nums1, nums2, i + 1, j + 1, cnt + 1, memo)
        cnt2 = self.dfs(nums1, nums2, i + 1, j, 0, memo)
        cnt3 = self.dfs(nums1, nums2, i, j + 1, 0, memo)

        # memo[(i, j, cnt)] = max(cnt1, max(cnt2, cnt3))
        return memo[(i, j, cnt)]