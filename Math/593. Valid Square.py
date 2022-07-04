class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 给4个点 看能否组成正方形 --> 算出每两个点之间的距离，最后只有两种可能，边长和斜边 + 要确保4个点是不重复的
        points = set()
        seen = set()

        total = [p1] + [p2] + [p3] + [p4]

        for i, (a, b) in enumerate(total):
            points.add((a, b))
            for j, (x, y) in enumerate(total):
                if i == j:
                    continue
                seen.add(abs(a - x) ** 2 + abs(b - y) ** 2)

        return len(seen) == 2 and len(points) == 4


