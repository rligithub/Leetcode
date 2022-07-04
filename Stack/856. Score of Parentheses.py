class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        stack.append(0)  # 用一个栈来维护当前所在的深度，以及每一层深度的score

        for char in s:
            if char == "(":
                stack.append(0)  # 遇到一个左括号 ( 时，我们将深度加一，并且新的深度的score 为 0
            else:
                score = stack.pop()
                stack[-1] += max(2 * score, 1)  # 遇到一个右括号 ) 时，我们将当前深度的score 乘二并加到上一层的深度

        return stack.pop()