class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # similar to 1339. Maximum Product of Splitted Binary Tree
        # if delete nodes --> remaining nodes == left child, right child, parents
        # parents nodes == total nodes - leftchild nodes - rightchild nodes
        # return number of nodes that have the highest score
        n = len(parents)
        graph = collections.defaultdict(list)  # {parent: child}
        for i in range(n):
            graph[parents[i]].append(i)

        counter = collections.defaultdict(int)
        self.dfs(graph, counter, 0)  # 求出每个结点作为根的子树的结点数

        res = []
        maxScores = 0
        for p in range(n):  # 遍历删去结点，计算counter[根结点]*counter[左孩子]*counter[右孩子]
            score = 1
            for child in graph[p]:  # CASE1: if deleted root, score = leftsubtree*rightsubtree
                score *= counter[child]
            if p != 0:  # CASE2: if deleted non-root, score = leftsubtree*rightsubtree*parent
                score *= n - counter[p]

            res.append(score)
            maxScores = max(maxScores, score)

        return res.count(maxScores)

    def dfs(self, graph, counter, root):  # 求出每个结点作为根的子树的结点数
        count = 1

        for child in graph[root]:
            count += self.dfs(graph, counter, child)

        counter[root] = count

        return count






