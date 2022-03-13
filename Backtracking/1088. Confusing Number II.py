class Solution:
    def confusingNumberII(self, n: int) -> int:
        # build graph --> save all valid nums
        # subset + permutation from valid nums --> see if it's in the range
        reverse = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        self.res = 0
        for num in ('1', '6', '8', '9'):
            self.dfs(reverse, n, num, reverse[num])
        return self.res

    def dfs(self, reverse, n, num1, num2):
        if num1 != num2:
            self.res += 1

        for num in reverse:
            if int(num1 + num) > n:
                continue
            self.dfs(reverse, n, num1 + num, reverse[num] + num2)