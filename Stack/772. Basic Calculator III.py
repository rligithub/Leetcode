class Solution:
    def __init__(self):
        self.i = 0

    def calculate(self, s: str) -> int:
        # 有 + - * / 和 ( )

        stack = []
        num = 0
        sign = "+"

        while self.i < len(s):
            ch = s[self.i]

            if ch.isdigit():
                num = num * 10 + int(ch)
            self.i += 1
            if ch == "(":
                num = self.calculate(s)
            if ch in "+-*/)" or self.i == len(s):  # 滞后性 需要把最后一个数字加入stack里
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = ch
            if ch == ")":
                break

        return sum(stack)