class Solution:
    def reverseVowels(self, s: str) -> str:

        word = list(s)
        vowels = "aeiou"
        left, right = 0, len(word) - 1

        while left <= right:
            if word[left].lower() in vowels and word[right].lower() in vowels:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1

            elif word[left].lower() in vowels and word[right].lower() not in vowels:
                right -= 1

            elif word[left].lower() not in vowels and word[right].lower() in vowels:
                left += 1

            else:
                left += 1
                right -= 1

        return "".join(word)