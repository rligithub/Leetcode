class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # binary search --> gcd --> check if there is n num are less than it
        mod = 10 ** 9 + 7

        left, right = min(a, b), min(a * n, b * n)

        while left <= right:
            mid = left + (right - left) // 2
            if self.getSmallerMagicalNum(a, b, mid) < n:
                left = mid + 1
            else:
                right = mid - 1
        return left % mod

    def getSmallerMagicalNum(self, a, b, target):

        return target // a + target // b - target // (a * b // math.gcd(a, b))
