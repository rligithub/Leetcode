class Solution:  # two pointers
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == "0":
                    return False
                size = 0
                while j < len(abbr) and abbr[j].isdigit():
                    size = size * 10 + int(abbr[j])
                    j += 1
                i += size
        return i == len(word) and j == len(abbr)