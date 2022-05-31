class Solution1:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        left, right = 0, 0

        path = []
        while left < len(encoded1) and right < len(encoded2):
            num = encoded1[left][0] * encoded2[right][0]
            size = min(encoded1[left][1], encoded2[right][1])

            path.append([num, size])
            encoded1[left][1] -= size
            encoded2[right][1] -= size

            if encoded1[left][1] == 0:
                left += 1
            if encoded2[right][1] == 0:
                right += 1

        res = []
        for i in range(len(path)):
            if i > 0 and path[i][0] == path[i - 1][0]:
                res[-1][1] += path[i][1]
                continue
            res.append([path[i][0], path[i][1]])

        return res


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        left, right = 0, 0

        res = []
        while left < len(encoded1) and right < len(encoded2):
            num = encoded1[left][0] * encoded2[right][0]
            size = min(encoded1[left][1], encoded2[right][1])

            if res and res[-1][0] == num:
                res[-1][1] += size
            else:
                res.append([num, size])
            encoded1[left][1] -= size
            encoded2[right][1] -= size

            if encoded1[left][1] == 0:
                left += 1
            if encoded2[right][1] == 0:
                right += 1

        return res 