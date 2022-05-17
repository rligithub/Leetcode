class Solution:  # template 1
    def search(self, nums: List[int], target: int) -> int:
        # search target
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
                # case 1 --> mid and target are in the same interval
            if target > nums[-1] and nums[mid] > nums[-1] or (target <= nums[-1] and nums[mid] <= nums[-1]):
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    # case2 --> mid and target are in the different interval --> target in left, mid in right
            elif target > nums[-1] and nums[mid] <= nums[-1]:
                right = mid - 1
            # case3 --> mid and target are in the different interval --> target in right, mid in left
            elif target <= nums[-1] and nums[mid] > nums[-1]:
                left = mid + 1

        if nums[left] == target:
            return left
        return -1


class Solution1:  # template 2
    def search(self, nums: List[int], target: int) -> int:
        # search target
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
                # case 1 --> mid and target are in the same interval
            if target >= nums[0] and nums[mid] >= nums[0] or (target < nums[0] and nums[mid] < nums[0]):
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
                    # case2 --> mid and target are in the different interval --> target in left, mid in right
            elif target >= nums[0] and nums[mid] < nums[0]:
                right = mid
                # case3 --> mid and target are in the different interval --> target in right, mid in left
            elif target < nums[0] and nums[mid] >= nums[0]:
                left = mid + 1

        if nums[left] == target:
            return left
        return -1


class Solution2:  # template 1
    def search(self, nums: List[int], target: int) -> int:
        # search target
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
                # mid is in left side
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # mid is in right side
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

