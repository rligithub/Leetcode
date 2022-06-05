class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.index = collections.defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.index[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        list1 = self.index[word1]
        list2 = self.index[word2]

        left, right = 0, 0
        res = float('inf')
        while left < len(list1) and right < len(list2):
            res = min(res, abs(list1[left] - list2[right]))
            if list1[left] > list2[right]:
                right += 1
            else:
                left += 1
        return res

    # Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)