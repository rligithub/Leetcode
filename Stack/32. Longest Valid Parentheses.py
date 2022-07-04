class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxx = 0
        stack = []
        stack.append(-1)  # initialization --> avoid first char is ")"

        for i in range(
                len(s)):  # remove all valid parentheses --> check cur i and last invalid index in stack to calculate
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maxx = max(maxx, i - stack[-1])
                else:
                    stack.append(i)

        return maxx