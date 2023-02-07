class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        summ = 0
        for i in range(k):
            summ += nums[i]

        res = summ
        for i in range(k, len(nums)):
            summ += nums[i] - nums[i - k]
            res = max(res, summ)

        return res / k


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window size k + two pointers

        l = 0
        summ = 0
        maxAvg = float('-inf')
        for r in range(len(nums)):
            summ += nums[r]
            if r - l + 1 >= k:
                maxAvg = max(maxAvg, summ / k)
                summ -= nums[l]
                l += 1

        return maxAvg
