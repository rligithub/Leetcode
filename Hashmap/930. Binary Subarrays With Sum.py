class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        table = collections.defaultdict(int)
        summ = 0
        res = 0
        table[0] = 1
        for i, num in enumerate(nums):
            summ += num
            if summ - goal in table:
                res += table[summ - goal]
            table[summ] += 1

        return res

