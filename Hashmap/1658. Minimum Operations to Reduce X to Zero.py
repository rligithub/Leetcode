class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # convert to a questions to get a longest subarray that summ = target
        if sum(nums) == x:
            return len(nums)

        target = sum(nums) - x
        table = {}
        table[0] = -1
        summ = 0
        res = 0

        for i, num in enumerate(nums):
            summ += num
            if summ - target in table:
                res = max(res, i - table[summ - target])
            table[summ] = i

        if res == 0:
            return -1
        else:
            return len(nums) - res


class Solution1:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        res = -1
        left, right = 0, 0
        summ = 0
        while left < n and right < n:
            if right < n:
                summ += nums[right]
                right += 1
            while summ > target and left < n:
                summ -= nums[left]
                left += 1

            if summ == target:
                res = max(res, right - left)

        return n - res if res >= 0 else -1