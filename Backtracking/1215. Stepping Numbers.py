class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        minsize = len(str(low))
        maxsize = len(str(high))

        res = []
        if low == 0:
            res.append(0)
        self.dfs(low, high, '', res, minsize, maxsize)
        res = sorted(res)
        return res

    def dfs(self, low, high, path, res, minsize, maxsize):

        if len(path) >= minsize and low <= int(path) <= high:
            res.append(int(path))

        for num in range(10):
            if not path and num == 0:  # no leading zero
                continue
            if not path or abs(int(path[-1]) - num) == 1:
                if len(path) <= maxsize and int(path + str(num)) <= high:
                    self.dfs(low, high, path + str(num), res, minsize, maxsize)


class Solution2:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        res = []
        if low == 0:
            res.append(0)

        for num in range(1, 10):
            self.dfs(high, low, num, res)

        res = sorted(res)
        return res

    def dfs(self, high, low, num, res):
        if num > high:
            return
        if num >= low:
            res.append(num)

        last = num % 10;
        if last > 0:
            self.dfs(high, low, 10 * num + last - 1, res)
        if last < 9:
            self.dfs(high, low, 10 * num + last + 1, res)


