class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        res = []
        while a or b:
            if len(res) >= 2 and res[-1] == res[-2]:
                writeA = res[-1] == 'b' # True or false
            else:
                writeA = a >= b     # True or false
            if writeA:
                a -= 1
                res.append('a')
            else:
                b -= 1
                res.append('b')

        return "".join(res)
