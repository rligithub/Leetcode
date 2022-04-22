class Solution:  # union find
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        holder = {}
        # union + save holder's name for each email ---> {email: holder}
        for account in accounts:
            if len(account) == 1:
                continue
            main_email = account[1]
            for email in account[1:]:
                holder[email] = account[0]
                uf.union(main_email, email)

        # find + build graph to save all connected emails together
        graph = collections.defaultdict(list)
        for email in holder:
            root = uf.find(email)
            graph[root].append(email)

            # print res
        res = []
        for email in graph:
            res.append([holder[email]] + sorted(graph[email]))
        return res


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, i):
        if i not in self.parent: # see parents
            self.parent[i] = i

        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
