class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()
        count = 0
        for i in range(n):
            if nums[i] * 3 > target:
                break
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    count += right - left
                    left += 1
                elif total >= target:
                    right -= 1
        return count