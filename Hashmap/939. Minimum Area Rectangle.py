class SolutionTLE:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # 先把y坐标一样的点存在一起，把x坐标一样的点存在一起
        # 固定对角线的a和b点，检查c和d点是否存在

        xtable = collections.defaultdict(list)
        for x, y in points:
            xtable[x].append(y)

        n = len(points)
        res = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2:  # find 对角线的a和b点
                    continue
                x3, y3 = x2, y1
                x4, y4 = x1, y2

                if x3 in xtable:
                    if y3 not in xtable[x3]:
                        continue
                if x4 in xtable:
                    if y4 not in xtable[x4]:
                        continue

                res = min(res, abs(x2 - x1) * abs(y2 - y1))

        if res == float('inf'):
            return 0
        return res


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # 先点存到set里,从没存的点里找一个a,再从set里找一个b,然后检查 第三个点c 和 第四个点d 是否在set里,是的话,直接求面积; 否则 把该点存到set里,继续
        # 已知固定对角线的a和b点，检查c和d点是否存在

        visited = set()

        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in visited:
                x3, y3 = x2, y1
                x4, y4 = x1, y2
                if (x3, y3) in visited and (x4, y4) in visited:
                    res = min(res, abs(x2 - x1) * abs(y2 - y1))
            visited.add((x1, y1))

        if res == float('inf'):
            return 0
        return res

