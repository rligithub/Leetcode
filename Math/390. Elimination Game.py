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




"""
1 2 3 4 5 6 7 8 9 10 11 12 13 14 -> head, step, remain
1 2 3 4 5 6 7 8 9 10 11 12 13 14 ->   1,    1,   14
  2   4   6   8   10    12    14 ->   2,    2,   7
      4       8         12       ->   4,    4,   3
              8                  ->   8,    8,   1

1 2 3 4 5 6 7 8 9 10 11 12 13    -> head, step, remain
1 2 3 4 5 6 7 8 9 10 11 12 13    ->   1,    1,   13
  2   4   6   8   10    12       ->   2,    2,   6
  2       6       10             ->   2,    4,   3
          6                      ->   6,    8,   1

从左删除: head + step
从右删除:
    odd remain: head + step. ie: 2, 4, 6
    even remain: head不变. ie: 2, 4, 6, 8
每次删除, 数字之间距离增加一倍，step ✖️ 2

"""


class Solution: # O（logn）
    def lastRemaining(self, n: int) -> int:
        head, step, remain = 1, 1, n
        is_left = True
        while remain != 1:
            # if from left or (from right but has odd numbers)
            if is_left or (not is_left and remain % 2 == 1):
                head += step
            remain //= 2
            step *= 2
            is_left = not is_left
            print(head, step, remain, is_left)
        return head