class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        table = collections.defaultdict(int)
        summ = 0
        res = 0
        mod = 10 ** 9 + 7

        for i, num in enumerate(arr):
            summ += num
            if summ % 2 == 1:
                res += table[0] + 1
                table[1] += 1
            else:
                res += table[1]
                table[0] += 1
        return res % mod
