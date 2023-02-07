class Solution:
    def maxProduct(self, s: str) -> int:
        # 先找出每个点的palindorme半径，然后找出两个最大的palindorme且不相交 --> return
        # manacher --> p[i] = max r at i

        t = s
        n = len(t)

        p = [0] * n
        maxRight = -1
        ctr = -1

        for i in range(n):
            if i <= maxRight:
                r = min(p[ctr * 2 - i], maxRight - i)
                while i - r >= 0 and i + r < n and t[i - r] == t[i + r]:
                    r += 1
                p[i] = r - 1
            else:
                r = 0
                while i - r >= 0 and i + r < n and t[i - r] == t[i + r]:
                    r += 1
                p[i] = r - 1
            if i + p[i] > maxRight:
                maxRight = i + p[i]
                ctr = i

                # left[i] ---> 以i为左边界能获得最大回文串
        # right[i] ---> 以i为右边界能获得最大回文串
        left = [0] * n
        right = [0] * n

        left[0] = 1
        j = 0
        for i in range(1, n):
            while j + p[j] < i:
                j += 1
            left[i] = max(left[i - 1], 2 * (i - j) + 1)

        right[-1] = 1;
        j = n - 1
        for i in range(n - 2, -1, -1):
            while j > 0 and j - p[j] > i:
                j -= 1
            right[i] = max(right[i + 1], 2 * (j - i) + 1)

        # find maxx
        res = 0
        for i in range(n - 1):
            res = max(res, left[i] * right[i + 1])

        return res









