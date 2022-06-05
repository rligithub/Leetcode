class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        left, right = 0, 0
        size = 0
        while left < len(word) and right < len(abbr):
            if abbr[right].isalpha():
                if word[left] != abbr[right]:
                    return False
                else:
                    left += 1
                    right += 1
            else:
                if abbr[right] == '0':
                    return False
                size = 0
                while right < len(abbr) and abbr[right].isdigit():
                    size = size * 10 + int(abbr[right])
                    right += 1
                left += size
        return left == len(word) and right == len(abbr)
