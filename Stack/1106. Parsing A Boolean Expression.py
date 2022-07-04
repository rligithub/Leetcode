class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for i in range(len(expression)):
            ch = expression[i]
            print(ch, stack)
            if ch == ")":
                seen = set()
                while stack[-1] != "(":
                    seen.add(stack.pop())
                stack.pop()  # '('

                sign = stack.pop()

                if sign == "!":
                    if "f" in seen:
                        stack.append("t")
                    else:
                        stack.append("f")
                elif sign == "&":
                    if "f" not in seen:
                        stack.append("t")
                    else:
                        stack.append("f")
                elif sign == "|":
                    if "t" in seen:
                        stack.append("t")
                    else:
                        stack.append("f")
            elif ch != ",":
                stack.append(ch)

        return stack.pop() == 't'








