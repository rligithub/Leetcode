class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # similar to 31
        # from right to left

        num = list(str(n))
        i, j = len(num) - 2, len(num) - 1

        while i >= 0 and num[i] >= num[i + 1]:
            i -= 1

        if i < 0:
            return -1

        while j >= 0 and num[i] >= num[j]:
            j -= 1

        num[i], num[j] = num[j], num[i]

        res = int("".join(num[:i + 1] + sorted(num[i + 1:])))
        if res <= 2 ** 31 - 1:
            return res
        return -1