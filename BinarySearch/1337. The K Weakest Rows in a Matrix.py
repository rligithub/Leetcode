class Solution1:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 注意 这道题的顺序是从1到0， 降序排列
        # 注意 这道题 要你求前k个strong到weak排列的row index
        # for loop each row --> find col index of last "1" --> res.append(col_index, row_index)
        # sort res --> print(res[:k])

        strong = []
        for i, row in enumerate(mat):
            count = self.findFirstPosition(row, 1)
            strong.append((count, i))

        strong.sort()
        res = []
        for count, index in strong:
            res.append(index)
        return res[:k]

    def findFirstPosition(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1


class Solution:
    def kWeakestRows(self, mat, k: int):
        m, n = len(mat), len(mat[0])
        row = []
        for i in range(m):
            row.append([sum(mat[i]), i])
        print(row)
        row.sort()
        res = []
        for i in range(k):
            res.append(row[i][1])
        return res