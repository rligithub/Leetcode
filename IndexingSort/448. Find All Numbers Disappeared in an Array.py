class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # similar to 41 first missing num

        n = len(nums)
        for i, num in enumerate(nums):
            index = abs(num)
            if index <= n:
                nums[index - 1] = -abs(nums[index - 1])

        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)

        return res


