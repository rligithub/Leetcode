class Solution:  # 比较每个word的同index上的char，如果前面相同，比较不同的那位。不同的时候 --> word1[i]:word2[i]
    def alienOrder(self, words: List[str]) -> str:
        # build graph
        graph = collections.defaultdict(set)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            find_diff = False
            for j in range(min(len(w1), len(w2))):
                c1, c2 = w1[j], w2[j]
                if c1 != c2:
                    graph[c1].add(c2)
                    find_diff = True
                    break
            if find_diff == False and len(w1) > len(w2):  # ab vs a --> invalid
                return ''
        print(graph)
        # print path
        self.res = []
        flag = {char: 0 for word in words for char in word}
        for char in flag:
            if flag[char] == 0: # unvisited
                if not self.dfs(graph, char, flag):
                    return ''
        return ''.join(self.res[::-1])

    def dfs(self, graph, i, flag):
        if flag[i] == -1:  # visited --> check has cycle
            return False
        if flag[i] == 1:  # backtrack --> finished check --> no cycle
            return True

        flag[i] = -1

        for nei in graph[i]:
            if not self.dfs(graph, nei, flag):
                return False
        flag[i] = 1  # backtracking --> no cycle
        self.res.append(i)
        return True

