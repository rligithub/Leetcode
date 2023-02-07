class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # word order can not be changed --> 需要填满整个rows毛球问需要几个sentence

        s = ' '.join(sentence) + ' '
        n = len(s)

        index = 0
        for _ in range(rows):
            index += cols
            # 不能fit就回到上个空格，后面的重新算
            while s[index % n] != ' ':
                index -= 1
            index += 1
        return index // n
