class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # if we have duplicated substring with large size --> we must have duplicates for smaller size
        # ony care about minSize

        hashmap = {}

        for i in range(len(s) - minSize + 1):
            word = s[i:i + minSize]
            if word in hashmap:
                hashmap[word] += 1
            else:
                count = Counter(word)
                if len(count) <= maxLetters:
                    hashmap[word] = 1

        res = 0
        for word in hashmap.keys():
            res = max(res, hashmap[word])
        return res
