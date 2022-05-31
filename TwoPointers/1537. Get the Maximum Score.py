class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        left, right = 0, 0
        mod = 10 ** 9 + 7
        score1, score2, maxscore = 0, 0, 0

        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                maxscore += nums1[left] + max(score1, score2)
                score1 = score2 = 0
                left += 1
                right += 1

            elif nums1[left] < nums2[right]:
                score1 += nums1[left]
                left += 1
            elif nums1[left] > nums2[right]:
                score2 += nums2[right]
                right += 1

        while left < len(nums1):
            score1 += nums1[left]
            left += 1
        while right < len(nums2):
            score2 += nums2[right]
            right += 1
        maxscore += max(score1, score2)
        return maxscore % mod
