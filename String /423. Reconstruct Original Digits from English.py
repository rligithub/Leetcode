class Solution:
    def originalDigits(self, s: str) -> str:
        # 把打算的英文字母组成的英文数字(0-9) 转换成数字，从大到小排列
        # 用hashmap来找数字，注意有些英文数字包含unique的char
        # zero, one, two, three, four, five, six, seven, eight, nine

        number = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                  "eight": "8", "nine": "9"}
        unique1 = {"z": "zero", "w": "two", "u": "four", "x": "six", "g": "eight"}
        unique2 = {"o": "one", "h": "three", "f": "five", "s": "seven"}
        unique3 = {"i": "nine"}
        count = collections.Counter(s)

        res = []
        for ch in unique1.keys():
            if ch in count:
                multiple = count[ch]
                word = unique1[ch]
                num = number[word] * multiple
                res.append(num)
                for ch in word:
                    count[ch] -= 1 * multiple
                    if count[ch] == 0:
                        del count[ch]
        for ch in unique2.keys():
            if ch in count:
                multiple = count[ch]
                word = unique2[ch]
                num = number[word] * multiple
                res.append(num)
                for ch in word:
                    count[ch] -= 1 * multiple
                    if count[ch] == 0:
                        del count[ch]

        for ch in unique3.keys():
            if ch in count:
                multiple = count[ch]
                word = unique3[ch]
                num = number[word] * multiple
                res.append(num)
                for ch in word:
                    count[ch] -= 1 * multiple
                    if count[ch] == 0:
                        del count[ch]

        res.sort()
        return "".join(res)



