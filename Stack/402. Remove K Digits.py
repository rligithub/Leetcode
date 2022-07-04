class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 维持一个递增的stack --> 遇到降序则pop stack中 大的数字
        # 两种情况： 1) pop的数字个数 比k 多    2)pop的数字个数 比k少,则要往前
        if k >= len(num):
            return "0"

        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k:  # if there is remaining k
            stack.pop()
            k -= 1

        res = []
        return str(int("".join(stack)))  # convert to integer to avoid leading zero