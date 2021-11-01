class Solution1:
    # 赛车 --》 A --> 起始速度为1，每次加速x2; R--> reset 起始速度 -1
    # THREE CASES to reach target
    # CASE1: go forward to reach target --> speed *= 2 ==> think about bit ===> step = 1 << 0...n
    # CASE2: go pass target + turn back to reach target
    # CASE3: go behind target + turn back + go forward to reach target

    def racecar(self, target: int) -> int:
        memo = {}
        return self.dfs(target, memo)

    def dfs(self, target, memo):
        if target in memo:
            return memo[target]

        # CASE 1 and 2
        pass_steps = target.bit_length()
        curpos1 = (1 << pass_steps) - 1
        if curpos1 == target:
            return pass_steps
        res = self.dfs(curpos1 - target, memo) + pass_steps + 1

        # CASE 3:
        behind_steps = pass_steps - 1
        curpos2 = (1 << behind_steps) - 1
        for back_steps in range(behind_steps):
            backdist = (1 << back_steps) - 1
            res = min(res, self.dfs(target - curpos2 + backdist, memo) + behind_steps + back_steps + 2)

        memo[target] = res
        return res
