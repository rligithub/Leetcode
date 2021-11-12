class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # 从subarry中删掉一个数字后 得到的 subarry最大sum 是多少
        memo = {}
        # res = float('-inf')
        # for i in range(len(arr)):
        #    res = max(res, self.dfs(arr, i, True, memo))
        # return res
        self.dfs(arr, 0, True, memo)
        return max(memo.values())

    def dfs(self, arr, pos, canDelete, memo):
        if (pos, canDelete) in memo:
            return memo[(pos, canDelete)]

        # 当有且只有一个值[-50]时，比较delete, not_delete, arr[0], delete 回返回一个base case。只能为负无穷
        if pos == len(arr):
            return float('-inf')

        delete = float('-inf')
        if canDelete:
            delete = self.dfs(arr, pos + 1, False, memo)

        not_delete = self.dfs(arr, pos + 1, canDelete, memo) + arr[pos]

        memo[(pos, canDelete)] = max(delete, not_delete, arr[pos])
        return memo[(pos, canDelete)]
