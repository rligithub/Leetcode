class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # binary search --> 最后一整轮的球的分值是k，寻找最大的k，使得分值大于等于k的球的总数不超过orders

        mod = 10 ** 9 + 7
        inventory.sort()

        left, right = 0, max(inventory)
        while left <= right:
            mid = left + (right - left) // 2
            if self.getGreaterCount(inventory, mid) <= orders:
                right = mid - 1
            else:
                left = mid + 1

        k = left
        res = 0
        sold = 0
        for inv in inventory[::-1]:
            if inv < k:
                break
            sold += inv - k + 1
            res += (inv - k + 1) * (inv + k) // 2  # 5 + 4 + 3 ==> k=3

        if sold < orders:
            res += (orders - sold) * (k - 1)

        return res % mod

    def getGreaterCount(self, inventory, k):

        res = 0
        for inv in inventory[::-1]:
            if inv < k:
                break
            res += inv - k + 1
        return res

