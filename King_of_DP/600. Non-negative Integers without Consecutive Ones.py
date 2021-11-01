class Solution1:  # TLE
    def findIntegers(self, n: int) -> int:
        # (bitmask << 1 ) & bitmask == 1: --> consective ones
        # (bitmask << 1 ) & bitmask == 0: --> NO consective ones

        res = 0
        for i in range(n + 1):
            if (i << 1) & i == 0:
                res += 1

        return res


class Solution:  # top down dp
    def findIntegers(self, n):
        # 如果前一位是1 --> 只能选0 --> restrict
        # 如果前一位是0 -->可以选 0 或 1 --> not restrict
        num = bin(n)[2:]

        memo = {}
        return self.dfs(num, 0, 0, True, memo)

    def dfs(self, num, i, prev, restrict, memo):
        if (i, prev, restrict) in memo:
            return memo[(i, prev, restrict)]

        if i == len(num):
            return 1

        res = 0

        if restrict:
            limit = int(num[i])
        else:
            limit = 1

        for digit in range(limit + 1):
            # 如果两个连续为1，skip
            if prev and digit:
                continue
            res += self.dfs(num, i + 1, digit, False if digit < limit else restrict, memo)

        memo[(i, prev, restrict)] = res
        return memo[(i, prev, restrict)]

