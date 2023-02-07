class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        # 先把所有的abb的单词放到一起，{abb:word1, word2.. }
        # 检查是否有哪个abb个数超过了2, 用recursion来计算下一个abb

        word2abbr = {}  # {word: abbr}
        self.getUniqueAbbrs(word2abbr, words, 0)  # abbr --> start from word[0] + size + word[-1]

        res = []
        for word in words:
            res.append(word2abbr[word])
        return res

    def getUniqueAbbrs(self, word2abbr, words, i):
        table = collections.defaultdict(list)  # {abbr: word}

        for word in words:
            abbr = self.getAbbr(word, i)
            table[abbr].append(word)

        for abbr, wordlist in table.items():
            if len(wordlist) == 1:
                word2abbr[wordlist[0]] = abbr
            else:
                self.getUniqueAbbrs(word2abbr, wordlist, i + 1)

    def getAbbr(self, word, i):
        if len(word) - i <= 3:
            return word
        return word[:i + 1] + str(len(word) - i - 2) + word[-1]