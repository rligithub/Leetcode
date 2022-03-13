class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        graph = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        if not digits:
            return []
        res = []
        path = []
        self.dfs(graph, digits, 0, n, path, res)
        return res

    def dfs(self, graph, digits, pos, n, path, res):
        if len(path) == n:  # 必须要每个数字里挑一个（len(path) == n)
            res.append(''.join(path))
            return

        for i in range(pos, n):
            for char in graph[digits[i]]:
                self.dfs(graph, digits, i + 1, n, path + [char], res)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        graph = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        if not digits:
            return []
        res = []
        path = []
        self.dfs(graph, digits, 0, n, path, res)
        return res

    def dfs(self, graph, digits, pos, n, path, res):
        if len(path) == n:  # 必须要每个数字里挑一个（len(path) == n)
            res.append(''.join(path[:]))
            return

        for i in range(pos, n):
            for char in graph[digits[i]]:
                path.append(char)
                self.dfs(graph, digits, i + 1, n, path, res)
                path.pop()



