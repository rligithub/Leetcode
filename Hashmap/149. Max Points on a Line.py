class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 以每个点为起点，其他点和这个点的斜率，如果斜率相同 则 ++ ---> hashmap，key == 起点， value = 斜率相同的点的个数

        n = len(points)
        res = 0
        for i in range(n):
            hashmap = collections.defaultdict(int)
            duplicates = 1
            for j in range(i + 1, n):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    duplicates += 1
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                delta = self.gcd(dx, dy)
                hashmap[(dx // delta, dy // delta)] += 1
            res = max(res, (max(hashmap.values()) if hashmap else 0) + duplicates)
        return res

    def gcd(self, x, y):
        if y == 0:
            return x
        else:
            return self.gcd(y, x % y)