class TreeAncestor1:  # TLE

    def __init__(self, n: int, parent: List[int]):
        self.hashmap = collections.defaultdict(int)
        for i in range(n):
            self.hashmap[i] = parent[i]

    def getKthAncestor(self, node: int, k: int) -> int:
        cnt = 0
        p = node
        while cnt != k and p != -1:
            p = self.hashmap[p]
            cnt += 1

        return p


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)


from sortedcontainers import SortedDict


class TreeAncestor2:  # topdown + binary search

    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        self.table = {}

    def getKthAncestorUtil(self, node: int, k: int):
        if k == 0:
            return node

        if node <= 0:
            return -1

        if node in self.table:
            if k in self.table[node]:
                return self.table[node][k]
            else:
                temp = self.table[node].bisect_left(k)
                if temp > 0:
                    prev = self.table[node].peekitem(temp - 1)
                    # print(prev)
                    self.table[node][k] = self.getKthAncestorUtil(prev[1], k - prev[0])
                    return self.table[node][k]

        self.table[node] = self.table.get(node, SortedDict())
        self.table[node][k] = self.getKthAncestorUtil(self.parent[node], k - 1)

        return self.table[node][k]

    def getKthAncestor(self, node: int, k: int) -> int:
        return self.getKthAncestorUtil(node, k)


class TreeAncestor6:
    def __init__(self, n: int, parent: List[int]):
        # dp[i][j] is node j's (1 << i) ancestor
        m = int(math.log2(n)) + 1
        self.dp = [parent if i == 0 else [-1] * n for i in range(m)]
        for k in range(1, m):
            for i in range(n):
                if self.dp[k - 1][i] == -1:
                    self.dp[k][i] = -1
                else:
                    self.dp[k][i] = self.dp[k - 1][self.dp[k - 1][i]]

    def getKthAncestor(self, node: int, k: int) -> int:
        while k:
            step = k & -k
            node = self.dp[int(math.log2(step))][node]
            k -= step
            if node == -1:
                break
        return node


class TreeAncestor:
    def __init__(self, n, parent):
        # build parents for 1, 2, 4, 8...2**n

        self.pars = [parent]
        self.n = n
        for k in range(int(math.log2(n))):
            row = []
            for i in range(n):
                p = self.pars[-1][i]
                if p != -1:
                    p = self.pars[-1][p]
                row.append(p)
            self.pars.append(row)

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        i = 0
        while k != 0 and node != -1:
            if (k & 1):
                node = self.pars[i][node]
            i += 1
            k >>= 1
        return node