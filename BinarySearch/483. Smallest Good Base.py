class Solution:
    def smallestGoodBase(self, n: str) -> str:

        num = int(n)
        # 枚举 k进制 中 1 的个数，最多为 二进制 时的位数
        for i in range(num.bit_length(), 2, -1):
            # k^0 + k^1 + …… + k^(i-1) = n -- 通过二分法计算 k
            # kn - n = k^i - 1
            left, right = 2, num - 1
            while left <= right:
                mid = (left + right) // 2
                s = mid * num - num - pow(mid, i) + 1
                if s == 0:
                    return str(mid)
                elif s > 0:
                    left = mid + 1
                else:
                    right = mid - 1
        return str(num - 1)

