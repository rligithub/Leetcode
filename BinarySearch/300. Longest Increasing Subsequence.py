class Solution:  # binary search
    def lengthOfLIS(self, nums: List[int]) -> int:
        # find cur_num insert position in res --> replace or append it in res
        res = []
        for num in nums:
            pos = self.findInsertposition(res, num)
            if pos < len(res):
                res[pos] = num
            else:
                res.append(num)
        return len(res)

    def findInsertposition(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

