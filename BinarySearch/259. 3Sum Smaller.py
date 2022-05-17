class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # 找右边界
        n = len(nums)

        nums.sort()
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[j] >= 0 and nums[j] + nums[i] >= target:
                    break
                left, right = j + 1, n - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if nums[mid] < target - nums[i] - nums[j]:
                        left = mid + 1

                    else:
                        right = mid - 1
                res += right - j
        return res

