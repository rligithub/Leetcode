class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # 求被两个rectangle cover的总共面积
        # step1: calculate areas of both rectangles, calculate area of intersection
        # step2: return areas of rectangle 1 + areas of rectangle 2 - areas of intersection

        rectangle1 = abs(ax1 - ax2) * abs(ay1 - ay2)
        rectangle2 = abs(bx1 - bx2) * abs(by1 - by2)

        w = max(0, min(ax2, bx2) - max(ax1, bx1))
        h = max(0, min(ay2, by2) - max(ay1, by1))

        overlap = w * h

        return rectangle1 + rectangle2 - overlap
