class Solution3:  # BFS --> check by level see if there is res in current level - slower
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = collections.deque()
        queue.append(s)
        visited = set()
        visited.add(s)
        res = []

        found = False
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if self.isValid(cur):
                    res.append(cur)
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        nxt = cur[:i] + cur[i + 1:]
                        if nxt not in visited:
                            queue.append(nxt)
                            visited.add(nxt)
            if res:
                return res

        return res

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


class Solution:  # BFS --> only find validpath, not need to check next level
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue = collections.deque()
        queue.append(s)
        visited = set()
        visited.add(s)
        res = []

        found = False
        while queue:
            cur = queue.popleft()
            if self.isValid(cur):
                found = True
                res.append(cur)
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        nxt = cur[:i] + cur[i + 1:]
                        if nxt not in visited:
                            queue.append(nxt)
                            visited.add(nxt)

        return res

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


