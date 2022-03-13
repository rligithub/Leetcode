class Solution3:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        supplies = collections.Counter(letters)

        needs = []
        s = [0] * len(words)
        for i, word in enumerate(words):
            count = collections.defaultdict(int)
            for ch in word:
                s[i] += score[ord(ch) - ord('a')]
                count[ch] += 1
            needs.append(count)

        memo = {}
        return self.dfs(words, needs, s, 0, supplies)

    def dfs(self, words, needs, score, i, supplies):
        if i >= len(words):
            return 0

        for ch in needs[i]:
            if needs[i][ch] > supplies[ch]:
                return self.dfs(words, needs, score, i + 1, supplies)

        for ch in words[i]:
            supplies[ch] -= 1
        pick = self.dfs(words, needs, score, i + 1, supplies) + score[i]
        for ch in words[i]:
            supplies[ch] += 1
        no_pick = self.dfs(words, needs, score, i + 1, supplies)
        return max(pick, no_pick)


class Solution1:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        supplies = collections.Counter(letters)
        return self.dfs(words, score, 0, supplies)

    def dfs(self, words, score, i, supplies):
        if i >= len(words):
            return 0

        word_count = collections.Counter(words[i])
        for ch in word_count:
            if word_count[ch] > supplies[ch]:
                return self.dfs(words, score, i + 1, supplies)

        for ch in words[i]:
            supplies[ch] -= 1
        pick = self.dfs(words, score, i + 1, supplies) + self.get_score(score, words[i])
        for ch in words[i]:
            supplies[ch] += 1
        no_pick = self.dfs(words, score, i + 1, supplies)
        return max(pick, no_pick)

    def get_score(self, score, word):
        val = 0
        for ch in word:
            val += score[ord(ch) - ord('a')]
        return val








