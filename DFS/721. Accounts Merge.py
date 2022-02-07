class Solution:  # dfs
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # build graph --> {main_email: connected emails}
        graph = collections.defaultdict(list)
        for account in accounts:
            if len(account) == 1:
                continue
            main_email = account[1]
            for email in list(set(account[2:])):
                graph[main_email].append(email)
                graph[email].append(main_email)

        res = []
        visited = set()
        for account in accounts:
            path = []
            name = account[0]
            main_email = account[1]
            if main_email not in visited:
                self.dfs(graph, main_email, path, visited)
            if path:
                res.append([name] + sorted(path))

        return res

    def dfs(self, graph, email, path, visited):

        visited.add(email)
        path.append(email)
        for nei in graph[email]:
            if nei not in visited:
                self.dfs(graph, nei, path, visited)


