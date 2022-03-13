class Solution:
    def addOperators(self, num: str, target: int):
        self.res = []
        self.dfs(num, target, 0, 0, 0, '')
        return self.res

    def dfs(self, nums, target, pos, prev, value, path):
        if pos == len(nums):
            if value == target:
                self.res.append(path)
            return

        for i in range(pos, len(nums)):
            if i > pos and nums[pos] == '0':  # no leading zero
                continue
            cur = int(nums[pos:i + 1])
            if pos == 0:
                self.dfs(nums, target, i + 1, cur, cur, path + str(cur))
            else:
                self.dfs(nums, target, i + 1, cur, value + cur, path + '+' + str(cur))
                self.dfs(nums, target, i + 1, - cur, value - cur, path + '-' + str(cur))
                self.dfs(nums, target, i + 1, prev * cur, (value - prev) + cur * prev, path + '*' + str(cur))

        # 2 + 6 * 7 --> prev = +6 , val = 8
        #           --> val - prev + prev * cur ===> val
        #           --> prev * cur ===> prev

