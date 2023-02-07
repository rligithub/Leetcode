class Solution1:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # hashmap
        hashmap = {}  # {word: index}
        for i, word in enumerate(words):
            hashmap[word] = i

        res = []
        for i, word in enumerate(words):
            reverse = word[::-1]
            if reverse in hashmap and i != hashmap[reverse]:
                res.append([i, hashmap[reverse]])

            for suff in self.findValidSuff(word):
                reverse = suff[::-1]
                if reverse in hashmap:
                    res.append([hashmap[reverse], i])

            for pref in self.findValidPref(word):
                reverse = pref[::-1]
                if reverse in hashmap:
                    res.append([i, hashmap[reverse]])

        return res

    def findValidSuff(self, word):
        validSuff = []
        for i in range(len(word)):
            if word[:i + 1] == word[:i + 1][::-1]:
                validSuff.append(word[i + 1:])

        return validSuff

    def findValidPref(self, word):
        validPref = []
        for i in range(len(word)):
            if word[i:] == word[i:][::-1]:
                validPref.append(word[:i])
        return validPref


class Solution2:
    def palindromePairs(self, words):
        table = {word: i for i, word in enumerate(words)}
        res = set()
        for i, word in enumerate(words):
            for k in range(len(word) + 1):
                a = word[:k]
                b = word[k:]

                if a == a[::-1] and b[::-1] in table and table[b[::-1]] != i:
                    res.add((table[b[::-1]], i))

                if b == b[::-1] and a[::-1] in table and table[a[::-1]] != i:
                    res.add((i, table[a[::-1]]))

        return list(res)


