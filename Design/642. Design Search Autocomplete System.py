class TrieNode:
    def __init__(self):
        self.children = dict()
        self.sentences = set()


class AutocompleteSystem:  # trie

    def __init__(self, sentences: List[str], times: List[int]):
        self.context = ''
        self.table = collections.defaultdict(int)  # {sentences: time}--> find top 3
        self.root = TrieNode()
        for s, t in zip(sentences, times):  # build trie for sentences
            self.table[s] = t
            self.addSentences(s)

        self.node = self.root

    def input(self, c: str) -> List[str]:
        res = []
        if c != '#':
            self.context += c
            if self.node:
                self.node = self.node.children.get(c)
            if self.node:
                res = sorted(self.node.sentences, key=lambda x: (-self.table[x], x))[:3]
        else:
            self.table[self.context] += 1
            self.addSentences(self.context)  # insert new sentences in trie
            self.context = ''
            self.node = self.root
        return res

    def addSentences(self, sentence):  # insert trie
        node = self.root
        for ch in sentence:
            if not node.children.get(ch):
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.sentences.add(sentence)

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)