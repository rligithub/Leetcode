class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        left, right = 0, 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1

        self.dfs(s, 0, left, right, res)
        return res

    def dfs(self, s, pos, lremove, rremove, res):
        if lremove < 0 or rremove < 0:
            return

        if lremove == 0 and rremove == 0:
            if self.isValid(s):
                res.append(s)
            return

        for i in range(pos, len(s)):
            if i > pos and s[i] == s[i - 1]:  # de-duplicated
                continue

            if lremove + rremove > len(s) - i:
                break

            if s[i] == '(':
                self.dfs(s[:i] + s[i + 1:], i, lremove - 1, rremove, res);

            if s[i] == ')':
                self.dfs(s[:i] + s[i + 1:], i, lremove, rremove - 1, res);

    def isValid(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0


class Solution1:  # TOO SLOW
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # step1 - pre-processing to see if we should remove "("    or     ")"
        # step2 - generate path, if s[pos] == parentheses_to_be_deleted, delete vs not_delete --> check if valid (pruning)

        res = []
        lremove, rremove = 0, 0
        for ch in s:
            if ch == '(':
                lremove += 1
            elif ch == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1
        path = ''
        valid = [-1]
        self.dfs(s, 0, lremove, rremove, path, res, valid)
        return list(set(res))

    def dfs(self, s, pos, lremove, rremove, path, res, valid):
        if lremove < 0 or rremove < 0:
            return
        if pos == len(s):
            if lremove == 0 and rremove == 0:
                res.append(path)
            return

        if s[pos] == '(':
            self.dfs(s, pos + 1, lremove - 1, rremove, path, res, valid)  # delete

        if s[pos] == ')':
            self.dfs(s, pos + 1, lremove, rremove - 1, path, res, valid)  # delete

        if self.isValid(s[pos], valid):
            self.dfs(s, pos + 1, lremove, rremove, path + s[pos], res, valid)  # not_delete
        self.backtrack(s[pos], valid)

    def isValid(self, char, valid):
        if char == '(':
            valid.append(1)
            return True
        if char == ')':
            if valid.pop() == -1 or not valid:
                return False
            return True
        else:
            return True

    def backtrack(self, char, valid):
        if char == ')':
            valid.append(1)
        if char == '(':
            valid.pop()
