class SolutionTLE:

    def __init__(self, n: int, blacklist: List[int]):
        self.block = set(blacklist)
        self.n = n

    def pick(self) -> int:
        num = random.randint(0, self.n - 1)
        while num not in self.block:
            num = random.randint(0, self.n - 1)
        return num

    # Your Solution object will be instantiated and called as such:


# obj = Solution(n, blacklist)
# param_1 = obj.pick()


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        self.upper = n - m  # 可选的数一共n-m个
        self.map = dict()  # 转换的哈希表，key：黑名单，val：转换的白名单
        i = self.upper  # 下一个可取的值
        bset = set(blacklist)
        for black in blacklist:  # 遍历黑名单
            if black < self.upper:  # 如果黑名单元素在[0,n-m),那么需要被转换
                while i in bset:
                    i += 1
                self.map[black] = i
                i += 1

    def pick(self) -> int:
        num = random.randint(0, self.upper - 1)

        return self.map.get(num, num)