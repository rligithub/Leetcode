class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        same = 0
        angles = []
        for p in points:
            if p == location:
                same += 1
            else:
                angles.append(atan2(p[1] - location[1], p[0] - location[0]))
        angles.sort()

        n = len(angles)
        for i in range(n):
            angles.append(angles[i] + 2 * pi)  # 加 360度，然后范围相当于变成了 [-pi, 3*pi]

        maxx = 0
        right = 0
        degree = angle * pi / 180

        for i in range(n):
            while right < n * 2 and angles[right] <= angles[i] + degree:
                right += 1
            maxx = max(maxx, right - i)
        return same + maxx
