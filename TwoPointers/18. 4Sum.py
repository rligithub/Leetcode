class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # similar to 3Sum

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] * 4 > target:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if nums[i] + nums[j] * 3 > target:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                self.twoSum(nums, i, j, res, target)
        return res

    def twoSum(self, nums, i, j, res, target):
        left, right = j + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[j] + nums[left] + nums[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                res.append([nums[i], nums[j], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
