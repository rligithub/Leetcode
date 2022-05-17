class Solution1:
    def search(self, nums: List[int], target: int) -> bool:
        # 和 33. 搜索旋转排序数组 不同的是，本题元素并不唯一
        # find target in a rotated sorted array --> check position of mid first

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            # deduplicated the same value, 特判 防止 [1,0,1,1,1] 0
            if nums[left] == nums[mid]:
                left += 1
                continue
            if nums[left] <= nums[mid]:  # mid in left
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
