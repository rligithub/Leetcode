class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


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

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if not node:
                return None
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if not node:
                return None
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)