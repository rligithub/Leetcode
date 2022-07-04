class Solution1:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        # x > 0 --> n/k - (k + 1)/2 > 0
        upper_limit = ceil((2 * n + 0.25) ** 0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            # x should be integer
            if (n - k * (k + 1) // 2) % k == 0:
                count += 1
        return count


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 1
        for k in range(2, n):  # k --> size of consecutive integers
            # summ = (a + a+k-1) * k/2
            a = (2 * n // k + 1 - k) // 2
            if a < 1:
                break
            elif n == (2 * a + k - 1) * k // 2:
                count += 1
        return count