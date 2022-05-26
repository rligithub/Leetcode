class Solution:# template 2
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # binary search to find a num --> to see if there is k num that is smaller than it
        m, n = len(mat), len(mat[0])
        left, right = 0, 0
        for i in range(m):
            left += mat[i][0]
            right += mat[i][-1]

        cur_sum = left
        while left < right:
            mid = left + (right - left) // 2
            count = self.getNumOfSmaller(mat, mid, 0, cur_sum, k)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    def getNumOfSmaller(self, mat, target, pos, summ, k):
        # use dfs to find num of summ less than target ---> use prefixsumm --> nxtSumm = summ - mat[i][0] + mat[i][j]
        if pos == len(mat):
            return 1

        count = 0
        for j in range(len(mat[0])):
            nxtSumm = summ + mat[pos][j] - mat[pos][0]
            if nxtSumm <= target:
                count += self.getNumOfSmaller(mat, target, pos + 1, nxtSumm, k)
                # 剪枝，否则会超时
                if count >= k:
                    return count
            else:
                break

        return count


class Solution: # template 1
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # binary search to find a num --> to see if there is k num that is smaller than it
        m, n = len(mat), len(mat[0])
        left, right = 0, 0
        for i in range(m):
            left += mat[i][0]
            right += mat[i][-1]

        cur_sum = left
        while left <= right:
            mid = left + (right - left) // 2
            count = self.getNumOfSmaller(mat, mid, 0, cur_sum, k)
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getNumOfSmaller(self, mat, target, pos, summ, k):
        # use dfs to find num of summ less than target ---> use prefixsumm --> nxtSumm = summ - mat[i][0] + mat[i][j]
        if pos == len(mat):
            return 1

        count = 0
        for j in range(len(mat[0])):
            nxtSumm = summ + mat[pos][j] - mat[pos][0]
            if nxtSumm <= target:
                count += self.getNumOfSmaller(mat, target, pos + 1, nxtSumm, k)
                # 剪枝，否则会超时
                if count >= k:
                    return count
            else:
                break

        return count

