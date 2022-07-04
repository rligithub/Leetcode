class Solution1:
    def mirrorReflection(self, p: int, q: int) -> int:
        while ((q & 1) == 0 and (p & 1) == 0):
            q >>= 1
            p >>= 1
        # p 为偶数
        if ((p & 1) == 0):
            return 2
        # q 为偶数
        if ((q & 1) == 0):
            return 0
        # p, q 都是奇数
        return 1


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # three cases: p odd, q even --> 0; p odd, q odd --> 1 ; p even, q odd --> 2
        # find gct --> p / q = n / m
        m, n = 1, 1
        while (m * p != n * q):
            n += 1
            m = n * q // p

        if m % 2 == 1 and n % 2 == 1:  # n odd, m odd
            return 1
        if m % 2 == 0 and n % 2 == 1:  # n odd, m even
            return 0
        if m % 2 == 1 and n % 2 == 0:  # n even, m odd
            return 2
        return -1