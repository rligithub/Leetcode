class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefSum = []
        mod = 10 ** 9 + 7
        for i in range(n):
            summ = 0
            for j in range(i, n):
                summ += nums[j]
                prefSum.append(summ)

        prefSum.sort()

        return sum(prefSum[left - 1: right]) % mod