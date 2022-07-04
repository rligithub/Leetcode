class Solution1:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # similar to word break 1 and word break 2
        dictionary = set(words)

        res = []

        for word in words:
            if not word:
                continue
            if self.dfs(word, dictionary, 0, {}):
                res.append(word)
        return res

    def dfs(self, word, dictionary, i, memo):
        if i in memo:
            return memo[i]
        if i > len(word) - 1:
            return True

        for k in range(i + 1, len(word) + 1):

            if word[i:k] != word and (word[i:k] in dictionary):
                if self.dfs(word, dictionary, k, memo):
                    memo[i] = True
                    return memo[i]
        memo[i] = False
        return False


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

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isWord


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

        @functools.lru_cache()
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if self.trie.search(prefix) and self.trie.search(suffix):
                    return True
                if self.trie.search(prefix) and dfs(suffix):
                    return True
            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res


