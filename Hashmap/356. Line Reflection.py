class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # 先找出x最大值和最小值,然后就能求出中间对称的位置, 再去检查对应的对称点是否是hashmap里
        maxx = float('-inf')
        minx = float('inf')

        seen = set()
        for x, y in points:
            maxx = max(maxx, x)
            minx = min(minx, x)
            seen.add((x, y))

        midx = (maxx + minx) / 2

        for x, y in points:
            copyx = (midx - x) + midx
            if (copyx, y) not in seen:
                return False

        return True

