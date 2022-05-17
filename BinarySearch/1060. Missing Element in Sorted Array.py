class Solution1:
    def missingElement(self, nums: List[int], k: int) -> int:
        # similar to 1539 kth missing positive nums
        # 1539 ask for kth missing num which start from 1, but this quetsion ask for kth missing num starts from nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            numOfMissing = nums[mid] - mid - nums[0]  # same to #1539, but replace "1" with nums[0]
            if numOfMissing < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k + (nums[0] - 1)  # same to #1539, but replace "1" with nums[0]


