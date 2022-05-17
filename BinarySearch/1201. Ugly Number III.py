class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        left, right = min(a, b, c), n * min(a, b, c)

        while left <= right:
            mid = left + (right - left) // 2
            if self.getSmallerCounts(mid, a, b, c) < n:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getSmallerCounts(self, num, a, b, c):

        count = 0
        count += num // a
        count += num // b
        count += num // c
        count -= num // (self.lcm(a, b))
        count -= num // (self.lcm(a, c))
        count -= num // (self.lcm(b, c))
        count += num // (self.lcm(self.lcm(a, b), c))
        return count

    def lcm(self, a, b):
        return a * b // math.gcd(a, b)

