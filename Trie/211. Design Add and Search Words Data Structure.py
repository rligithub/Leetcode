class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(0, node, word)

    def dfs(self, i, node, word):
        if i == len(word):
            return node.isWord

        char = word[i]

        if char == '.':
            for child in node.children:
                path_validity = self.dfs(i + 1, node.children[child], word)
                if path_validity == True:
                    return True
            return False

        else:
            if char in node.children:
                return self.dfs(i + 1, node.children[char], word)
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)