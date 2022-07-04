class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b

        if b == 0:
            return a

        while b != 0:
            carry = a
            a = a ^ b
            b = b & carry
            b = b << 1

        return a


class Solution1:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0xffffffff

        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a & mask if b > mask else a
