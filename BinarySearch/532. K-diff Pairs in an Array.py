class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        count = 0
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:  # deduplicated
                continue
            left, right = i + 1, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == k + nums[i]:
                    count += 1
                    break
                elif nums[mid] > k + nums[i]:
                    right = mid - 1
                else:
                    left = mid + 1
        return count