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

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # max points you can observed from location

        # calculate angles of each point from location
        same = 0
        arr = []
        for x, y in points:
            if x == location[0] and y == location[1]:   # point is in the same location
                same += 1
                continue
            a = math.atan2(y - location[1], x - location[0])
            arr.append(a)
            arr.append(a + 2*math.pi)
        arr.sort()

        count = 0
        i = 0
        # for loop each angles, check to see if angles[j] - angles[i] <= angle, calculate max count of j - i + 1
        for j in range(len(arr)):
            while arr[j] - arr[i] > angle * math.pi / 180:
                i += 1
            count = max(count, j - i + 1)

        return count + same

