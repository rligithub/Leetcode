class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children.get(char)
        node.isWord = True

    def findStart(self, word):
        node = self.root
        for i, char in enumerate(word):  # word is longer than prefix ---> return prefix
            if node.isWord:
                return word[:i]
            if char not in node.children:
                return word
            node = node.children.get(char)
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        res = []
        for word in sentence.split():
            replace = trie.findStart(word)
            res.append(replace)
            # print(word, replace)
        return " ".join(res)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    def search(self, word):
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return False
        return node.isWord


class SolutionTony:
    def replaceWords(self, dictionary, sentence: str) -> str:
        s = sentence.split()
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        res = []
        for word in s:
            flag = False
            for i in range(len(word)):
                # if we found one, flad turns to True
                if trie.search(word[:i]):
                    res.append(word[:i])
                    flag = True
                    break
            # if we never found one, add the original word
            if not flag:
                res.append(word)
        return " ".join(res)