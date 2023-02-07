class Solution:
    def __init__(self):
        self.i = 0

    def calculate(self, s: str) -> int:
        # 只有 + - * /

        stack = []
        num = 0
        sign = "+"

        while self.i < len(s):
            ch = s[self.i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch == "(":
                num = self.calculate(s)
            if ch in "+-*/)" or self.i == len(s) - 1:  # 滞后性 需要把最后一个数字加入stack里
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
            self.i += 1
        return sum(stack)


class Solution:
    def __init__(self):
        self.i = 0

    def calculate(self, s: str) -> int:
        # 只有 + - * /

        stack = []
        num = 0
        sign = "+"

        while self.i < len(s):
            ch = s[self.i]

            if ch.isdigit():
                num = num * 10 + int(ch)
            self.i += 1     #######
            if ch == "(":
                num = self.calculate(s)
            if ch in "+-*/)" or self.i == len(s):  # 滞后性 需要把最后一个数字加入stack里 ######
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


class Solution:
    def calculate(self, s):
        stack = []
        num = 0
        sign = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = char
        return sum(stack)


class Solution:
    def calculate(self, s: str) -> int:
        return self.dfs(s, 0)

    def dfs(self, s, i):
        stack = []
        num = 0
        sign = "+"

        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in "+-*/)" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                if sign == "*":
                    stack.append(stack.pop() * num)
                if sign == "/":
                    stack.append(int(stack.pop() / num))

                num = 0
                sign = ch
            i += 1
        return sum(stack)