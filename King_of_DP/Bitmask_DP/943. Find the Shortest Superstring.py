class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        # 先求出每个单词到另一个单词的距离（第二个重复部分的长度不打印）
        # 假设所有单词还没被打印的状态是 1111 --> 全打印完的状态是0000
        # for loop每个起始点，求打印的path最短长度
        # 用dfs求path --> base case第一个单词，recursive 第二三个单词（不重复打印中间部分）

        # 求每个单词和单词间相同的char个数
        n = len(words)
        graph = [[0] * n for _ in range(n)]
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                for k in range(min(len(word1), len(word2)), -1, -1):
                    if word1[-k:] == word2[:k]:
                        graph[i][j] = k
                        break
        # --> TSP问题， 对于每个初始city，哪种travel路线 距离最短 （dfs存的是path）
        memo = {}
        res = ''
        for pos in range(n):
            path = self.dfs(graph, words, (1 << n) - 1, pos, memo)
            if res == '' or len(path) < len(res):
                res = path
        return res

    def dfs(self, graph, words, state, i, memo):
        # state --> state of full mask --> 11111
        # i --> index of word
        # graph --> table of num of same char between each words
        if (state, i) in memo:
            return memo[(state, i)]

        # 最后一个状态对应的单词
        if state == (1 << i):
            return words[i]

        res = ''
        for j in range(len(graph)):
            # Not the same word + 找出下一个对应的j能满足条件（unvisited）
            if j != i and state & (1 << j):
                # 注意是j到i的位置，因为第二个不打印重复值，i是第二个打印的
                path = self.dfs(graph, words, state ^ (1 << i), j, memo) + words[i][graph[j][i]:]  # 打印下一个单词重复之后的char
                if res == '' or len(path) < len(res):
                    res = path
        memo[(state, i)] = res
        return memo[(state, i)]


class Solution1:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        table = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(min(len(words[i]), len(words[j])), -1, -1):
                    if words[i][-k:] == words[j][:k]:
                        table[i][j] = k
                        break

        memo = {}
        res = ''
        for pos in range(n):
            path = self.dfs(words, table, (1 << n) - 1, pos, memo)
            if res == '' or len(path) < len(res):
                res = path
        return res

    def dfs(self, words, table, state, i, memo):
        if (state, i) in memo:
            return memo[(state, i)]

        if state == (1 << i):
            return words[i]

        res = ''
        for j in range(len(words)):
            if j != i and state & (1 << j):
                path = self.dfs(words, table, state ^ (1 << i), j, memo) + words[i][table[j][i]:]
                if res == '' or len(path) < len(res):
                    res = path
        memo[(state, i)] = res
        return memo[(state, i)]


a = Solution()
words = ['abc', 'bcde', 'cdef']
print(a.shortestSuperstring(words))