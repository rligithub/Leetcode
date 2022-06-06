class Solution:  # sliding window
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        res = []
        k, n = len(words), len(words[0])
        need = Counter(words)

        for i in range(len(s) - k * n + 1):
            temp = copy.deepcopy(need)
            count = 0
            for j in range(i, len(s), n):
                nxtWord = s[j:j + n]
                if nxtWord not in temp or temp[nxtWord] <= 0:
                    break
                temp[nxtWord] -= 1
                count += 1
                if count == k:
                    res.append(i)
        return res


