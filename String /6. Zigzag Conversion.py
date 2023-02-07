class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 标记 --> 1234 3 2 1 234..
        if numRows == 1 or numRows >= len(s):
            return s

        res = [""] * numRows
        index, dire = 0, 0

        for char in s:
            res[index] += char
            if index == 0:
                dire = 1
            elif index == numRows - 1:
                dire = -1
            index += dire

        return "".join(res)