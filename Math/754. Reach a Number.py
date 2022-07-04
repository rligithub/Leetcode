class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        left, right = 0, target
        # 取比连续数之和小的第一个尾数，右边界不变，左边界递增
        while left < right:
            mid = left + (right - left) // 2
            summ = mid * (mid + 1) // 2
            if summ >= target:
                right = mid
            else:
                left = mid + 1
        summ = left * (left + 1) // 2
        # 差值为偶数，将(sum - target) // 2这个数符号变成负
        if not (summ - target) % 2:
            return left
        # 差值为奇数，且步数为偶数，则下一步一定是奇数，下一步的sum和target的差值一定是偶数，与上面相同
        elif not left % 2:
            return left + 1
        # 差值为奇数，且步数为奇数，则下一步一定是偶数，下两步一定是奇数(下两步的和一定为奇数)，下两步的sum和target的差值一定是偶数，与上面相同
        else:
            return left + 2

