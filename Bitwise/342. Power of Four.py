class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # similar to 231
        # find power of two --> n & (n -1) == 0 ---> 100 & 011 = 0
        # (3+1)^x ---> 3^x + 1 ---> n % 3 == 1

        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
