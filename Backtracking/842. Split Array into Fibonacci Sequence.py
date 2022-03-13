class Solution1:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        # split array 至少分三段，前两段的和 为第三段

        res = []
        path = []
        if self.dfs(num, path, res):
            return res
        return []

    def dfs(self, num, path, res):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False

        if not num and len(path) >= 3 and path[-1] == path[-2] + path[-3]:
            res.extend(path)
            return True

        for i in range(1, len(num) + 1):
            if (i == 1 or num[0] != '0') and int(num[:i]) < 2 ** 31:
                if self.dfs(num[i:], path + [int(num[:i])], res):
                    return True
        return False


class Solution:  # slower
    def splitIntoFibonacci(self, num: str) -> List[int]:
        # split array 至少分三段，前两段的和 为第三段

        self.res = []
        path = []

        self.dfs(num, path)
        return self.res

    def dfs(self, num, path):

        if not num and len(path) >= 3 and path[-1] == path[-2] + path[-3]:
            self.res = path
            return

        for i in range(1, len(num) + 1):
            if (i == 1 or num[0] != '0') and int(num[:i]) < 2 ** 31:
                if len(path) < 3 or path[-1] == path[-2] + path[-3]:
                    self.dfs(num[i:], path + [int(num[:i])])

