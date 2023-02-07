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

class Solution: # local index
    def calculate(self, s: str) -> int:

        return self.dfs(s, 0)

    def dfs(self, s, i):
        stack = []
        num = 0
        sign = '+'

        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = 10 * num + int(ch)

            if ch == '(':
                num, i = self.dfs(s, i+1)
            if ch in "+-*/)" or i == len(s) -1:   # +-*/)
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                if ch == ')':
                    return sum(stack), i
                sign = ch
            i += 1
        return sum(stack)


