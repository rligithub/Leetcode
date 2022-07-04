class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        points = sorted(trees)  # from left to right 从最左边开始

        lower = []
        upper = []

        for point in points:
            while len(lower) >= 2 and self.crossProduct(lower[-2], lower[-1], point) < 0:
                lower.pop()
            while len(upper) >= 2 and self.crossProduct(upper[-2], upper[-1], point) > 0:
                upper.pop()
            lower.append(tuple(point))  # 把所有下曲线的点 都放进来
            upper.append(tuple(point))  # 把所有上曲线的点 都放进来

        return list(set(lower + upper))  # 找出曲线这些点（去掉重复的点）

    def crossProduct(self, p1, p2, p3):  # 算向量的角度--> (p3-p2) 和 (p2-p1) 比较
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)

