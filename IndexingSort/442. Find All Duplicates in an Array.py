class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 每个数字出现一次或者两次，打印所有出现两次以上的数字

        nums.sort()

        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                res.append(nums[i])
        return res


class Solution:# indexing
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            index = abs(num)
            if nums[index - 1] < 0:  # second time(repeated num appears) --> check if it's negative
                res.append(index)
            else:
                nums[index - 1] = -nums[index - 1]  # first time --> mark all to negative

        return res

