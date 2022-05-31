class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # 注意 题目要求 只能改变一次 --> 比较长度来判断怎么改变

        sizeS, sizeT = len(s), len(t)

        i, j = 0, 0
        while i < sizeS and j < sizeT and s[i] == t[j]:
            i += 1
            j += 1
        if i == sizeS and j == sizeT:
            return False

        if sizeS == sizeT:
            # Update
            i, j = i + 1, j + 1
        elif sizeS < sizeT:
            # Insert
            j += 1
        else:
            # Delete
            i += 1

        while i < sizeS and j < sizeT and s[i] == t[j]:
            i += 1
            j += 1
        return i == sizeS and j == sizeT
