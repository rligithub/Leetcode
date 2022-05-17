'''
https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/solution/793-jie-cheng-han-shu-hou-kge-ling-er-fe-ont9/
'''


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # 对于一个数n，其阶乘n！末尾0的个数可以通过求解n中包含的因子5的个数得到。

        # 题目要求末尾0的个数为K的n的个数，可以从区间[low, high]中搜索，对每个搜索到的数字n都判断其末尾0的个数是否为K，但这样太慢，可以用二分搜索改进搜索效率。

        # 如果存在n！使末尾0的个数为K，则会有5个数同时满足题目要求，因为每变化5，末尾才会加一个0。因此，如果能找到末尾0的个数为5的n！，则必有5个数满足要求，return 5。不能找到则return 0

        left, right = k, k * 10

        while left <= right:
            mid = (left + right) // 2
            count = self.num_zeros(mid)
            if count == k:
                return 5
            elif count < k:
                left = mid + 1
            else:
                right = mid - 1
        return 0

    def num_zeros(self, n):
        res = 0
        div = 5
        while n >= div:
            res += n // div
            div = div * 5
        return res


