class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        for i in range(len(expression) - 1, -1, -1):
            if stack and stack[-1] == "?":
                stack.pop()  # ?
                first = stack.pop()  # first num
                stack.pop()  # :
                second = stack.pop()  # second num
                if expression[i] == "T":
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(expression[i])

        return stack[0]