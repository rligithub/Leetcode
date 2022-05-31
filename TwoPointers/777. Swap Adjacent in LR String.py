
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # L只能左移，R只能右移
        # 把X看作空格，L只能在空格中左移，R只能在空格中右移
        n = len(start)
        i, j = 0, 0

        while i < n and j < n:
            while i < n and start[i] == "X":
                i += 1
            while j < n and end[j] == "X":
                j += 1

            if i < n and j < n:
                if start[i] != end[j] or (i < j and start[i] == "L") or (i > j and end[j] == "R"):
                    return False
                else:
                    i += 1
                    j += 1

        while i < n and start[i] == "X":
            i += 1
        while j < n and end[j] == "X":
            j += 1

        return i == j
