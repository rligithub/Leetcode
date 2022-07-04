class Solution:
    def lastRemaining(self, n: int) -> int:
        # 从左边往右 移除，每隔一个 移除一个， 接着从右往左移动，每隔一个 移动一个 --> 交替移除,直到只剩一个数字为止
        # array = 1 2 3 4 5 6 7 8 9
        # remaining = 2 4 6 8 -----> 2*(1 2 3 4)

        # Take out 2 common:
        # newArray = 1 2 3 4
        # remaining = 2 * newArray
        # newArray will be sent in another recursion for answer

        if (n == 1):
            return 1
        print(n)
        return 2 * ((n // 2 - self.lastRemaining(n // 2)) + 1)