class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        queue = collections.deque()

        for i in range(1, 10):
            queue.append((i, str(i)))

        res = []
        while queue:
            cur, path = queue.popleft()

            if len(path) == n:
                res.append(int(path))
            for i in range(10):
                if len(path) < n and abs(int(path[-1]) - i) == k:
                    queue.append((i, path + str(i)))

        return res