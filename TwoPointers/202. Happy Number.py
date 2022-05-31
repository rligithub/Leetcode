class Solution1:
    def isHappy(self, n: int) -> bool:

        while n != 1 and n != 4:
            n = self.get_next(n)

        return n == 1

    def get_next(self, n):
        summ = 0
        while n != 0:
            digit = n % 10
            n = n // 10
            summ += digit ** 2
        return summ


class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.nxt(n)
        while slow != fast:
            slow = self.nxt(slow)
            fast = self.nxt(self.nxt(fast))

        return slow == 1

    def nxt(self, n):
        summ = 0
        while n != 0:
            digit = n % 10
            n = n // 10
            summ += digit ** 2
        return summ