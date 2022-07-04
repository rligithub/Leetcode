class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children.get(ch)
        node.isWord = True


class MagicDictionary:
    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        node = self.trie.root
        return self.dfs(node, searchWord, 0, 1)

    def dfs(self, node, word, i, k):
        if k < 0:
            return False

        if i == len(word):
            return k == 0 and node.isWord

        ch = word[i]
        if ch in node.children:
            if self.dfs(node.children[ch], word, i + 1, k):
                return True

        for child in node.children:
            if ch != child and self.dfs(node.children[child], word, i + 1, k - 1):
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)