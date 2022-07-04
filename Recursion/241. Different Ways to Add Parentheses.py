class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # edge case
        if expression.isdigit():
            return [int(expression)]

        res = []
        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                print(left, right)
                for x in left:
                    for y in right:
                        res.append(self.compute(x, y, expression[i]))

        return res

    def compute(self, x, y, op):
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y