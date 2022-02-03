class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        n = len(bottom)

        # build graph #
        graph = collections.defaultdict(list)
        for string in allowed:
            graph[string[:2]].append(string[-1])

        # do dfs --> for loop each two char, build next row --> until only one char #
        memo = {}
        return self.dfs(graph, 0, bottom, '', memo)

    def dfs(self, graph, i, cur_row, nxt_row, memo):
        if (i, cur_row, nxt_row) in memo:
            return memo[(i, cur_row, nxt_row)]

        if len(cur_row) == 1:
            return True
        if i == len(cur_row) - 1:
            return self.dfs(graph, 0, nxt_row, '', memo)
        char = cur_row[i:i + 2]
        if char not in graph:
            return False

        for nei in graph[char]:
            if self.dfs(graph, i + 1, cur_row, nxt_row + nei, memo):
                memo[(i, cur_row, nxt_row)] = True
                return True
        memo[(i, cur_row, nxt_row)] = False
        return False