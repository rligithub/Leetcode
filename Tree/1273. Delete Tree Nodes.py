class Solution1:  # TLE
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        # graph {parent: children}
        graph = collections.defaultdict(list)
        for i in range(nodes):
            if parent[i] == -1:
                node = value[i]  # record root
            else:
                graph[value[parent[i]]].append(value[i])

        # dfs --> subtree summ == 0 , delete
        summ, count = self.dfs(graph, node)
        return count

    def dfs(self, graph, root):

        summ = root
        count = 1
        for child in graph[root]:
            val, cnt = self.dfs(graph, child)
            summ += val
            count += cnt
        if summ == 0:
            count = 0

        return summ, count


class Solution1:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        # graph {parent index: children index}
        graph = collections.defaultdict(list)
        for i in range(nodes):
            graph[parent[i]].append(i)

        # dfs --> subtree summ == 0 , delete
        summ, count = self.dfs(value, graph, 0)
        return count

    def dfs(self, value, graph, root):

        summ = value[root]
        count = 1
        for child in graph[root]:
            val, cnt = self.dfs(value, graph, child)
            summ += val
            count += cnt
        if summ == 0:
            count = 0

        return summ, count 