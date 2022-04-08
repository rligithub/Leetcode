class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        queue = collections.deque()
        queue.append(('0000', 0))
        visited = set()
        visited.add('0000')

        while queue:
            cur, step = queue.popleft()

            if cur == target:
                return step

            for i in range(4):
                if cur[i] == '0':
                    next1 = cur[:i] + '1' + cur[i + 1:]
                    next2 = cur[:i] + '9' + cur[i + 1:]
                elif cur[i] == '9':
                    next1 = cur[:i] + '0' + cur[i + 1:]
                    next2 = cur[:i] + '8' + cur[i + 1:]
                else:
                    next1 = cur[:i] + str(int(cur[i]) + 1) + cur[i + 1:]
                    next2 = cur[:i] + str(int(cur[i]) - 1) + cur[i + 1:]
                if next1 not in visited and next1 not in deadends:
                    queue.append((next1, step + 1))
                    visited.add(next1)
                if next2 not in visited and next2 not in deadends:
                    queue.append((next2, step + 1))
                    visited.add(next2)
        return -1


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        visited = set(deadends)
        if '0000' in visited:
            return -1
        queue = collections.deque()
        queue.append(('0000', 0))
        visited.add('0000')

        while queue:
            cur, step = queue.popleft()

            if cur == target:
                return step

            for i in range(4):
                if cur[i] == '0':
                    next1 = cur[:i] + '1' + cur[i + 1:]
                    next2 = cur[:i] + '9' + cur[i + 1:]
                elif cur[i] == '9':
                    next1 = cur[:i] + '0' + cur[i + 1:]
                    next2 = cur[:i] + '8' + cur[i + 1:]
                else:
                    next1 = cur[:i] + str(int(cur[i]) + 1) + cur[i + 1:]
                    next2 = cur[:i] + str(int(cur[i]) - 1) + cur[i + 1:]
                if next1 not in visited:
                    queue.append((next1, step + 1))
                    visited.add(next1)
                if next2 not in visited:
                    queue.append((next2, step + 1))
                    visited.add(next2)
        return -1