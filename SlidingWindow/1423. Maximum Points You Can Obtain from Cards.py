class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)
        windowSize = n - k  # 窗口的大小
        sums = 0
        res = float("inf")  # 正无穷大
        for i in range(n):
            sums += cardPoints[i]
            if i >= windowSize:
                sums -= cardPoints[i - windowSize]
            if i >= windowSize - 1:
                res = min(res, sums)
        return sum(cardPoints) - res


class Solution1:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)
        left, right = 0, 0
        windowSize = n - k
        summ = 0
        minWindow = float('inf')
        total = 0

        while right < n:
            total += cardPoints[right]
            summ += cardPoints[right]
            if right - left + 1 > windowSize:
                summ -= cardPoints[left]
                left += 1
            if right - left + 1 == windowSize:
                minWindow = min(minWindow, summ)
            right += 1
        return total - minWindow


