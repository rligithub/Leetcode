class Solution1:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 每个数字出现两次，只有一个数字出现一次-->且时候sorted array
        # -> mid 偶数--> 如果mid的左边和mid相同value，则往左找，否则往右找 --> mid奇数 反之
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 0:  # even
                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid

        return nums[right]


class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 每个数字出现两次，只有一个数字出现一次-->且时候sorted array
        # array长度肯定为奇数 --> 如果mid的左边和mid相同value，则往左找，否则往右找
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == nums[mid ^ 1]:  # 使用异或来进行统一，因为 偶数异或1 等于 加1，奇数异或1 等于 减1
                left = mid + 1
            else:
                right = mid

        return nums[right]


class Solution1:  # bit operation
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res