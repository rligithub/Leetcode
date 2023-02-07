class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 有个数字missing被相同的数字取代了 --> 求重复的数字 和 missing的数字
        dup = -1
        missing = 1
        for num in nums:
            index = abs(num)
            if nums[index - 1] < 0:
                dup = index
            else:
                nums[index - 1] = - nums[index - 1]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1

        return [dup, missing]
