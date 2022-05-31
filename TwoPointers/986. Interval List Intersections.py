class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left, right = 0, 0
        res = []
        while left < len(firstList) and right < len(secondList):
            if firstList[left][1] < secondList[right][0]:
                left += 1
            elif firstList[left][0] > secondList[right][1]:
                right += 1
            else:
                res.append(
                    [max(firstList[left][0], secondList[right][0]), min(firstList[left][1], secondList[right][1])])
                if firstList[left][1] < secondList[right][1]:
                    left += 1
                else:
                    right += 1

        return res


