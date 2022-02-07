class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # swap后 smallest string是什么
        # step1: build graph

        graph = collections.defaultdict(list)

        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        # step2: 把连接的index存起来，找出对应的char，分别sort一下。replace原先的string
        visited = set()
        res = list(s)
        for i in range(len(s)):
            if i not in visited:
                swap_node = []
                self.dfs(graph, i, swap_node, visited)
                swap_node.sort()
                swap_char = []
                for idx in swap_node:
                    swap_char.append(res[idx])
                swap_char.sort()
                print(i, swap_node, swap_char)
                for j, ch in zip(swap_node, swap_char):
                    res[j] = ch

        return ''.join(res)

    def dfs(self, graph, i, swap_node, visited):
        visited.add(i)
        swap_node.append(i)
        for nei in graph[i]:
            if nei not in visited:
                self.dfs(graph, nei, swap_node, visited)

