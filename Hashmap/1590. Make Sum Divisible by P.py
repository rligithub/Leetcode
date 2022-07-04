class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # similar to #974
        need = sum(nums) % p
        table = {0: -1}
        presum = 0
        n = len(nums)
        res = len(nums)
        for i, num in enumerate(nums):
            presum = (presum + num) % p
            table[presum] = i
            if (presum - need) % p in table:
                res = min(res, i - table[(presum - need) % p])
        return res if res < n else -1