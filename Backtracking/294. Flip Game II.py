class Solution:  # dp
    def canWin(self, currentState: str) -> bool:
        memo = {}
        return self.dfs(currentState, memo)

    def dfs(self, state, memo):
        if state in memo:
            return memo[state]

        for i in range(len(state) - 1):
            if state[i:i + 2] == '++':
                if not self.dfs(state[:i] + '--' + state[i + 2:], memo):
                    memo[state] = True
                    return True
        memo[state] = False
        return False


class Solution1:  # dfs
    def canWin(self, currentState: str) -> bool:

        currentState = list(currentState)
        return self.dfs(currentState)

    def dfs(self, state):

        for i in range(len(state) - 1):
            if state[i] == '+' and state[i + 1] == '+':
                if not self.dfs(state[:i] + ['-', '-'] + state[i + 2:]):
                    return True
        return False


class Solution2:  # backtracking
    def canWin(self, currentState: str) -> bool:

        currentState = list(currentState)
        return self.dfs(currentState)

    def dfs(self, state):

        for i in range(len(state) - 1):
            if state[i] == '+' and state[i + 1] == '+':
                state[i] = '-'
                state[i + 1] = '-'
                nxt = self.dfs(state)
                state[i] = '+'
                state[i + 1] = '+'
                if not nxt:
                    return True
        return False