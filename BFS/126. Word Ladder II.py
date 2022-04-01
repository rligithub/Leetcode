class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 跟 word ladderI 比较：
        # 1）需要每层每层来加不同path --> 每层单词1对应的下一层单词 可以和 同层的单词2的下一层单词 重复 --> 层间去重就行
        # 2）需要打印这一层所有的path
        dicts = set(wordList)
        queue = collections.deque()
        visited = set()

        queue.append((beginWord, [beginWord]))
        visited.add(beginWord)
        res = []
        while queue:
            size = len(queue)
            seen = set()
            for i in range(size):
                word, path = queue.popleft()
                if word == endWord:
                    res.append(path)
                for nei in self.findNeighbors(word, dicts):
                    if nei not in visited:
                        queue.append((nei, path + [nei]))
                        seen.add(nei)
            visited |= seen

        return res

    def findNeighbors(self, word, dicts):
        res = []

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + c + word[i + 1:]
                if newWord in dicts:
                    res.append(newWord)
        return res
