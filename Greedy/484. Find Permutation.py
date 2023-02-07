class Solution1:
    def findPermutation(self, s: str) -> List[int]:
        # stack --> append i+1, each time see "I" pop num in stack (代表之前都是“D"，打印出reverse order)
        res = []
        stack = []
        s += "I"

        for i, ch in enumerate(s):
            stack.append(i + 1)
            if ch == "I":
                while stack:
                    res.append(stack.pop())

        return res


class SolutionTony:
    def findPermutation(self, s: str) -> List[int]:
        # stack --> append i+1, each time see "I" pop num in stack (代表之前都是“D"，打印出reverse order)
        res = []
        stack = []

        for i, ch in enumerate(s):
            stack.append(i + 1)
            if ch == "I":
                while stack:
                    res.append(stack.pop())
        stack.append(len(s) + 1)
        while stack:
            res.append(stack.pop())
        return res 