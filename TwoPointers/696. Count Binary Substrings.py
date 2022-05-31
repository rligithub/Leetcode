class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0  # 注意这个赋值
        res = 0
        i = 0
        for j, c in enumerate(s):
            if c != s[i]:
                res += min(count, j - i)
                count = j - i
                i = j
        res += min(count, len(s) - i)
        return res


class SolutionT:
    def countBinarySubstrings(self, s: str) -> int:

        stack = []
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])
        res = 0
        for i in range(1, len(stack)):
            res += min(stack[i - 1][1], stack[i][1])
        return res