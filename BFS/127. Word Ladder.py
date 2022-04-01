class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        dicts = set(wordList)
        queue = collections.deque()
        visited = set()

        queue.append((beginWord, 1))
        visited.add(beginWord)

        while queue:
            word, count = queue.popleft()
            if word == endWord:
                return count
            for nei in self.findNeighbors(word, dicts):
                if nei not in visited:
                    queue.append((nei, count + 1))
                    visited.add(nei)
        return 0

    def findNeighbors(self, word, dicts):
        res = []

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + c + word[i + 1:]
                if newWord in dicts:
                    res.append(newWord)

        return res
