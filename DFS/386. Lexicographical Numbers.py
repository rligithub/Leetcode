class Solution1:
    def lexicalOrder(self, n: int) -> List[int]:

        self.res = []
        for i in range(1, 10):
            self.dfs(i, n)
        return self.res

    def dfs(self, cur, n):
        if cur > n:
            return
        self.res.append(cur)
        for i in range(0, 10):
            num = cur * 10 + i
            if num <= n:
                self.dfs(num, n)


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.res = []
        self.dfs(1, n)
        return self.res

    def dfs(self, cur, n):
        # base case
        if cur > n:
            return
        self.res.append(cur)

        # CASE1: last digit is 0 - 9 ===> 5 next is 50 check if there is next digist for n
        self.dfs(cur * 10, n)

        # CASE2: last digit is 0 - 8 ===> 10 next is 11; 9 next is 90
        if cur % 10 != 9:
            self.dfs(cur + 1, n)
