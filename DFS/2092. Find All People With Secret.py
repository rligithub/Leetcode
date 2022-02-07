class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # return all people who know the secrets after meetings --> in any order

        # step1: build graph --> hashmap --> sort by meeting time --> {time: {a:c, b}, {b:c}, {c:a}}
        meetings.sort(key=lambda x: x[2])
        graph = {}
        for u, v, time in meetings:
            if time not in graph:
                graph[time] = collections.defaultdict(list)
            graph[time][u].append(v)
            graph[time][v].append(u)

        print(graph)
        # step2: for loop each time, check if people in meeting know the secrets, if not, mark as knew
        visited = set()
        visited.add(0)
        visited.add(firstPerson)
        for time in sorted(graph.keys()):
            for pp in graph[time]:
                if pp in visited:
                    self.dfs(graph[time], pp, visited)

        return list(visited)

    def dfs(self, mapping, node, visited):
        visited.add(node)
        for nei in mapping[node]:
            if nei not in visited:
                self.dfs(mapping, nei, visited)

