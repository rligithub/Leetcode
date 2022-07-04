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

    def search(self, prefix):
        node = self.root
        res = set()
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        self.dfs(node, prefix, res)
        return res

    def dfs(self, node, path, res):
        if node.isWord:
            res.add(path)

        for ch in node.children:
            self.dfs(node.children[ch], path + ch, res)


class WordFilter:
    def __init__(self, words: List[str]):
        self.table = {word: i for i, word in enumerate(words)}
        self.cache1 = {}
        self.cache2 = {}
        self.trie1 = Trie()
        self.trie2 = Trie()
        for word in words:
            self.trie1.insert(word)
            self.trie2.insert(word[::-1])

    def f(self, prefix: str, suffix: str) -> int:
        if prefix in self.cache1:
            words1 = self.cache1[prefix]
        else:
            words1 = self.trie1.search(prefix)
            self.cache1[prefix] = words1

        if suffix in self.cache2:
            words2 = self.cache2[suffix]
        else:
            words2 = [word[::-1] for word in self.trie2.search(suffix[::-1])]
            self.cache2[suffix] = words2
        words = set(words1) & set(words2)
        res = -1
        for word in words:
            res = max(res, self.table[word])
        return res

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)