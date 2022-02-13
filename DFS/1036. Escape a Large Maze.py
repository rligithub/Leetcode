class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        # 两种cases
        # 1）其中一个点被blocked住，那么被包围的最大面积为 （两条边的三角形） size*size/2
        # 2) 如果其中一个点没被包围住，则检查另一个点有没被包围住
        # 如果都没被包围 --> 肯定能找到 两个个点

        if not blocked:
            return True

        # maximum area that can be surrounded by 200 blockers (when they form a triangle with grid's corner)
        n = len(blocked) * len(blocked) // 2

        # build a hashset to store all blocks
        blocks = set()
        for (x, y) in blocked:
            blocks.add((x, y))

        return self.dfs(source[0], source[1], blocks, target, set(), n) & self.dfs(target[0], target[1], blocks, source,
                                                                                   set(), n)

    def dfs(self, i, j, blocks, target, visited, n):
        if (i == target[0] and j == target[1]) or len(visited) >= n:  # 有可能跑到一半就返回 True （没跑到终点）
            return True

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < 10 ** 6 and 0 <= y < 10 ** 6 and (x, y) not in blocks and (x, y) not in visited:
                if self.dfs(x, y, blocks, target, visited, n):
                    return True

        return False

