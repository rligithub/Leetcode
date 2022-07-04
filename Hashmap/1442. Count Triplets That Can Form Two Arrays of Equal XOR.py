class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # 求异或和为0的连续子数组
        res = 0
        n = len(arr)
        for i in range(n - 1):
            summ = arr[i]
            for j in range(i + 1, n):
                summ ^= arr[j]
                if summ == 0:
                    res += j - i
        return res