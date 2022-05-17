class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # subarry summ --> prefix summ
        n = len(nums)
        prefsum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefsum[i] = prefsum[i - 1] + nums[i - 1]

        res = float('inf')
        for i in range(1, n + 1):
            left, right = i, n
            while left <= right:
                mid = left + (right - left) // 2

                if prefsum[mid] >= target + prefsum[i - 1]:  # greater or equal to
                    res = min(res, mid - i + 1)
                    right = mid - 1
                elif prefsum[mid] < target + prefsum[i - 1]:
                    left = mid + 1

        if res < float('inf'):
            return res
        return 0
