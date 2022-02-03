class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # 如果同行或者同列存在，则可以删掉这个点。求最多可以删掉几个点 --> similar to num of islands
        # step1: 总共几个点
        # step2： 总共有几块不在同行或者同列 --> 每次删剩下一个
        # step3 : 最多删掉几个 ---> 即 总共的点 - 总共的块数（每块剩一个）

        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)

        visited = set()

        count = 0
        for i, j in stones:
            if (i, j) not in visited:
                count += 1
                self.dfs(rows, cols, visited, i, j)

        return len(stones) - count

    def dfs(self, rows, cols, visited, i, j):
        for col in rows[i]:
            if (i, col) not in visited:
                visited.add((i, col))
                self.dfs(rows, cols, visited, i, col)

        for row in cols[j]:
            if (row, j) not in visited:
                visited.add((row, j))
                self.dfs(rows, cols, visited, row, j)