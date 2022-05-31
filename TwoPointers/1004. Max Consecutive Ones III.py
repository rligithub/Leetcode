class Solution:  # two pointers
    def longestOnes(self, nums: List[int], k: int) -> int:
        # longest subarry that includes k zeros

        zeroCount = 0
        count = 0
        left, right = 0, 0

        while right < len(nums):
            if nums[right] == 0:
                zeroCount += 1
            right += 1
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            count = max(count, right - left)

        return count 