class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # similar to 31
        # from right to left
        # 从低位到高位找到第一个不满足升序的数字 (from right to left)
        # swap 到i位 --> 剩下来的第i位之后 按照降序排列即可

        num = list(str(n))
        i, j = len(num) - 2, len(num) - 1

        while i >= 0 and num[i] >= num[i + 1]:  # 从右往左找，找出第一个 比后面小的数 作为left --> 87254
            i -= 1

        if i < 0:
            return -1

        while j >= 0 and num[i] >= num[j]:  # 从右往左找，找出最小的比 left大的数，作为right
            j -= 1

        num[i], num[j] = num[j], num[i]  # swap left 和 right

        res = int("".join(num[:i + 1] + sorted(num[i + 1:])))  # left之后的数 按大小排列
        if res <= 2 ** 31 - 1:
            return res
        return -1


