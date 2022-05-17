class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        # do binary search to guess the kth + 1 smallest sum --> check if there is k num less than it
        # if yes --> search right, else --> search left

        left, right = 0, sum(nums)

        while left <= right:
            mid = left + (right - left) // 2
            if self.getSmallerNum(nums, mid) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getSmallerNum(self, nums, target):
        # two pointers to get num of smaller
        i = curSum = res = 0
        for j in range(len(nums)):
            curSum += nums[j]
            while curSum > target:
                curSum -= nums[i]
                i += 1
            res += j - i + 1
        return res
