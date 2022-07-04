class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 1000 & 0111 --> 0
        # similar to 342

        return n > 0 and n & (n - 1) == 0