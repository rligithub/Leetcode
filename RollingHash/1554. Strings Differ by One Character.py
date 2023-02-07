class Solution1:
    def differByOne(self, dict: List[str]) -> bool:
        # 给一组单词，求是否存在两个单词的只差一个character
        # step1: save all hashcodes in list
        # step2: for loop each index of word, newhashcode = hashcodes - current char * power , check if newhashcode exist in a set

        codes = []
        base = 26
        n = len(dict)

        for word in dict:
            hashcode = 0
            for ch in word:
                num = ord(ch) - ord("a")
                hashcode = hashcode * base + num
            codes.append(hashcode)

        k = len(dict[0])
        power = 1
        for i in range(k - 1, -1, -1):  # 从后往前，power *= 26， 否则 power的值需要 //26
            seen = set()
            for j in range(n):
                ch = dict[j][i]
                num = ord(ch) - ord("a")
                newhash = codes[j] - num * power
                if newhash in seen:
                    return True
                seen.add(newhash)
            power *= base

        return False


class SolutionMLE:  # hashset
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()

        for word in dict:
            for i in range(len(word)):
                wordcode = word[:i] + "*" + word[i + 1:]
                if wordcode in seen:
                    return True
                seen.add(wordcode)
        return False
