class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table = {}
        table[0] = -1
        res = 0
        count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in table.keys():
                res = max(res, i - table[count])
            else:
                table[count] = i

        return res 