class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        table = {}
        res = 0
        a, e, i, o, u = 0, 0, 0, 0, 0

        table["00000"] = -1
        for j in range(len(s)):
            ch = s[j]
            if ch == "a":
                a += 1
            elif ch == "e":
                e += 1
            elif ch == "i":
                i += 1
            elif ch == "o":
                o += 1
            elif ch == "u":
                u += 1
            string = str(a % 2) + str(e % 2) + str(i % 2) + str(o % 2) + str(u % 2)
            if string in table:
                res = max(res, j - table[string])
            else:
                table[string] = j
        return res


class Solution1:
    def findTheLongestSubstring(self, s: str) -> int:

        table = collections.defaultdict(int)
        table[0] = -1
        count = [0] * 5
        res = 0
        for i in range(len(s)):
            if s[i] == 'a':
                count[0] += 1
            elif s[i] == 'e':
                count[1] += 1
            elif s[i] == 'i':
                count[2] += 1
            elif s[i] == 'o':
                count[3] += 1
            elif s[i] == 'u':
                count[4] += 1
            key = self.convert(count)
            if key in table:
                res = max(res, i - table[key])
            else:
                # if key never there before, we add this key, because we want the largest bandwith
                table[key] = i
        return res

    def convert(self, count):
        key = 0
        for i in range(5):
            if count[i] % 2 == 1:
                key += (1 << i)
        return key