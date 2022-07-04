class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        table = collections.defaultdict(int)
        table[0] = 1
        res = 0
        summ = 0

        for num in nums:
            summ = (summ + num) % k
            res += table[summ]
            table[summ] += 1

        return res
