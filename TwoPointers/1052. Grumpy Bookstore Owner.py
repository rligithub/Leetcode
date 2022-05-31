class Solution1:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # fixed sliding window for minutes size

        summ = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                summ += customers[i]
        res = 0

        for i in range(len(customers)):
            if grumpy[i] == 1:
                summ += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                summ -= customers[i - minutes]
            res = max(res, summ)
        return res


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # fixed sliding window for minutes size

        summ = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                summ += customers[i]
        res = 0
        left, right = 0, 0
        while right < len(customers):
            if grumpy[right] == 1:
                summ += customers[right]
            right += 1
            while right - left > minutes:
                if grumpy[left] == 1:
                    summ -= customers[left]
                left += 1
            res = max(res, summ)
        return res
