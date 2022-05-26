class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        diff = float('inf')
        res = 0
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < diff:
                    diff = abs(total - target)
                    res = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                elif total == target:
                    return total

        return res