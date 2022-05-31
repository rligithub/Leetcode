class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        return self.findMost(nums, goal) - self.findMost(nums, goal - 1)

    def findMost(self, s, k):
        if k < 0:
            return 0
        summ = 0
        count = 0
        left, right = 0, 0

        while right < len(s):
            summ += s[right]

            while summ > k:
                summ -= s[left]
                left += 1
            count += right - left + 1
            right += 1
        return count