class Solution2:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        queue = collections.deque()
        queue.append((s1, 0))
        visited = set()
        visited.add(s1)

        while queue:
            cur, count = queue.popleft()
            if cur == s2:
                return count

            for nxt in self.findnxt(cur, s2):
                if nxt not in visited:
                    queue.append((nxt, count + 1))
                    visited.add(nxt)

        return -1

    def findnxt(self, string, target):
        res = []
        i = 0
        while string[i] == target[i]:
            i += 1

        for j in range(i + 1, len(target)):
            if string[j] == target[i]:
                temp = list(string)
                temp[i], temp[j] = temp[j], temp[i]
                temp = "".join(temp)
                res.append(temp)

        return res


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0

        queue = collections.deque()
        queue.append((s1, 0))
        visited = set()
        visited.add(s1)

        while queue:
            cur, count = queue.popleft()
            if cur == s2:
                return count

            i = 0
            while cur[i] == s2[i]:
                i += 1

            for j in range(i + 1, len(s2)):
                if cur[j] != s2[i]:
                    continue

                nxt = list(cur)
                nxt[i], nxt[j] = nxt[j], nxt[i]
                nxt = "".join(nxt)

                if nxt not in visited:
                    queue.append((nxt, count + 1))
                    visited.add(nxt)

        return -1  