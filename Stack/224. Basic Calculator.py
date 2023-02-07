class Solution1:# stack
    def calculate(self, s: str) -> int:
        # 只有（ ） 和+ -
        stack = []
        num = 0
        res = 0
        sign = 1 # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():
                num = (num * 10) + int(ch)

            elif ch == '+':
                res += sign * num
                sign = 1
                num = 0

            elif ch == '-':
                res += sign * num
                sign = -1
                num = 0

            elif ch == '(':
                stack.append(res)
                stack.append(sign)

                sign = 1
                res = 0

            elif ch == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0

        return res + sign * num


class Solution:  # stack + recusive

    def __init__(self):
        self.i = 0

    def calculate(self, s: str) -> int:
        # 只有 + - 和 ( )

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


class SolutionTony2:
    def __init__(self):
        self.i = 0

    def calculate(self, s):
        stack = []
        num = 0
        op = '+'

        while self.i < len(s):
            ch = s[self.i]
            self.i += 1
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch == '(':
                num = self.calculate(s)
            if self.i >= len(s) or ch == '+' or ch == '-' or ch == ')':
                if op == '+':
                    stack.append(int(num))
                else:
                    stack.append(-int(num))
                op = ch
                num = 0
            if ch == ')':
                break

        return sum(stack)


class Solution: # local index
    def calculate(self, s: str) -> int:
        # + - ( ) " "

        return self.dfs(s, 0)

    def dfs(self, s, i):
        num = 0
        stack = []
        sign = "+"

        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ch == "(":
                num, i = self.dfs(s, i + 1)
            if ch in "+-)" or i == len(s)-1:
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                num = 0
                if ch == ")":
                    return sum(stack), i

                sign = ch
            i += 1
        return sum(stack)