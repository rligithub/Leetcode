class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 先求出所有小rectangle的面积，然后求最大rectangle的面积，比较是否相同 并且大rectangle的四个顶点 只能出现一次（用hashset来存）
        points = set()

        minx, miny, maxx, maxy = float('inf'), float('inf'), 0, 0
        small_rectangles = 0
        for x, y, a, b in rectangles:
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, a)
            maxy = max(maxy, b)
            small_rectangles += (a - x) * (b - y)

            self.checkCorner(x, y, points)
            self.checkCorner(a, b, points)
            self.checkCorner(x, b, points)
            self.checkCorner(a, y, points)

        large_rectangles = (maxx - minx) * (maxy - miny)

        self.checkCorner(minx, miny, points)
        self.checkCorner(minx, maxy, points)
        self.checkCorner(maxx, miny, points)
        self.checkCorner(maxx, maxy, points)

        if len(points) != 0:
            return False

        return small_rectangles == large_rectangles

    def checkCorner(self, x, y, seen):
        if (x, y) in seen:
            seen.remove((x, y))
        else:
            seen.add((x, y))


class Solution1:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corner = set()
        X0 = Y0 = inf
        X1 = Y1 = -inf
        for x0, y0, x1, y1 in rectangles:
            area += (x1 - x0) * (y1 - y0)
            X0 = min(x0, X0)
            Y0 = min(y0, Y0)
            X1 = max(x1, X1)
            Y1 = max(y1, Y1)
            corner ^= {(x0, y0), (x0, y1), (x1, y0), (x1, y1)}
        return area == (X1 - X0) * (Y1 - Y0) and corner == {(X0, Y0), (X0, Y1), (X1, Y0), (X1, Y1)}