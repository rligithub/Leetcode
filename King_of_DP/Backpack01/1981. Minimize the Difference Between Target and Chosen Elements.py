class Solution1:  # TLE
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        memo = {}
        return self.dfs(mat, target, 0, memo)

    def dfs(self, mat, target, row, memo):
        if (target, row) in memo:
            return memo[(target, row)]

        if row == len(mat):
            return abs(target)

        res = float('inf')
        for num in mat[row]:
            res = min(res, self.dfs(mat, target - num, row + 1, memo))

        memo[(target, row)] = res
        return res


class Solution2:  # TLE
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        memo = {}
        return self.dfs(mat, target, 0, 0, memo)

    def dfs(self, mat, target, cursum, row, memo):
        if (cursum, row) in memo:
            return memo[(cursum, row)]

        if row == len(mat):
            return abs(cursum - target)

        res = float('inf')
        for num in mat[row]:
            res = min(res, self.dfs(mat, target, cursum + num, row + 1, memo))

        memo[(cursum, row)] = res
        return res


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:

        memo = {}
        # deduplicate in each row - 同一行中重复的数字 没有必要再算
        mat = map(set, mat)
        # sort each row
        mat = list(map(sorted, mat))
        return self.dfs(mat, target, 0, memo)

    def dfs(self, mat, target, row, memo):
        if (target, row) in memo:
            return memo[(target, row)]

        if row == len(mat):
            return abs(target)

        res = float('inf')
        for num in mat[row]:
            res = min(res, self.dfs(mat, target - num, row + 1, memo))
            if target - num < 0:
                break

        memo[(target, row)] = res
        return res











