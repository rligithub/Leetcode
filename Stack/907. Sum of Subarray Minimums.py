"""
huifeng

3, 1, 2, 4

xxxxxxx[xxxx y xxx]xxxxxx
      j      i     k

"""


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        mod = 10 ** 9 + 7
        res = 0
        stack = []  # non-decreasing
        arr = [float('-inf')] + arr + [float('-inf')]
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                cur = stack.pop()
                res += arr[cur] * (i - cur) * (cur - stack[-1])

            stack.append(i)
        return res % mod

