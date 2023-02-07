class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 比较两个数，但是要检查3个数 看需要改变的是当前数cur还是前一个数prev

        count = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if count == 1:
                    return False
                count += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] == nums[i]  # 改前一个数
                else:
                    nums[i] = nums[i - 1]  # 改当前的数
        return True

