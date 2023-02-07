class Solution:
    def countPrimes(self, n: int) -> int:
        # 求 n以内的质数 有几个 -->
        # 开一个n的空间，[1]*n --> 用index分别表示质数，第零个和第1个设为 0 --> 如果当前的数为1，则以当前的i为最小公约数，往后for loop，每次跳动i个，把它标记为0，以此类推 当前数的取值范围为（2，（根号n） +1 ），最后计算这个list中有几个1，则表示有几个质数

        if n < 3:
            return 0

        digits = [1] * n
        digits[0] = digits[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if digits[i] == 1:
                for j in range(i + i, n, i):
                    digits[j] = 0

        return sum(digits)