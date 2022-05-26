class Solution1:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        # 二分出 average 之后，把数组中的每个数都减去 average，然后的任务就是去求这个数组中，是否有长度 >= k 的 subarray，他的和超过 0
        # binary search average --> check if there is valid
        left, right = min(nums), max(nums)

        while left + 10 ** (-5) < right:
            mid = left + (right - left) / 2
            if self.isvalid(presum, mid, k):
                left = mid
            else:
                right = mid

        return left

    def isvalid(self, presum, avg, k):
        n = len(presum)
        minn = float("inf")
        for i in range(n - k):
            minn = min(minn, presum[i] - i * avg)
            if presum[i + k] - (i + k) * avg - minn >= 0:
                return True
        return False


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # 二分出 average 之后，把数组中的每个数都减去 average，然后的任务就是去求这个数组中，是否有长度 >= k 的 subarray，他的和超过 0
        # binary search average --> check if there is valid
        left, right = min(nums), max(nums)

        while left + 10 ** (-5) < right:
            mid = left + (right - left) / 2
            if self.isvalid(nums, mid, k):
                left = mid
            else:
                right = mid

        if self.isvalid(nums, right, k):
            return right
        return left

    def isvalid(self, nums, average, k):
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num - average)

        minn = 0
        for i in range(k, len(nums) + 1):
            if presum[i] - minn >= 0:
                return True
            minn = min(minn, presum[i - k + 1])

        return False