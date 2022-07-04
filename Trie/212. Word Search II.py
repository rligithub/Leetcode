class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isWord


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for word in words:
            trie.insert(word)
        m, n = len(board), len(board[0])

        def dfs(node, i, j, path, res):
            if node.isWord:
                res.append(path)
                node.isWord = False

            if i < 0 or j < 0 or i >= m or j >= n:
                return
            ch = board[i][j]
            node = node.children.get(ch)
            if not node:
                return
            temp = board[i][j]
            board[i][j] = "#"
            dfs(node, i + 1, j, path + ch, res)
            dfs(node, i - 1, j, path + ch, res)
            dfs(node, i, j + 1, path + ch, res)
            dfs(node, i, j - 1, path + ch, res)
            board[i][j] = temp

        res = []

        for i in range(m):
            for j in range(n):
                node = trie.root
                dfs(node, i, j, "", res)
        return res

class Solution1: # TLE
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                self.dfs(board, node, i, j, m, n, "", res)
        return res

    def dfs(self, board, node, i, j, m, n, path, res):

        if node.isWord:
            res.append(path)
            node.isWord = False

        if i < 0 or j < 0 or i >= m or j >= n:
            return
        node = node.children.get(board[i][j])
        if not node:
            return
        temp = board[i][j]
        board[i][j] = "#"
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x = i + dx
            y = j + dy
            self.dfs(board, node, x, y, m, n, path + temp, res)
        board[i][j] = temp