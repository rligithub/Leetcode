class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # find first position
        n = len(nums)
        nums.sort()
        res = -1
        for i in range(n):
            left, right = i + 1, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                summ = nums[mid] + nums[i]
                if summ < k:
                    res = max(res, summ)
                    left = mid + 1
                else:
                    right = mid - 1

        return res