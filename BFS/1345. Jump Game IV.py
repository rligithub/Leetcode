class Solution1:  # TLE
    def minJumps(self, arr: List[int]) -> int:
        # build graph --> {val: inddex}
        n = len(arr)
        graph = collections.defaultdict(list)

        for i, num in enumerate(arr):
            graph[num].append(i)

        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        visited.add(0)

        while queue:
            cur_index, step = queue.popleft()

            if cur_index == n - 1:
                return step

            for nxt_index in [cur_index + 1, cur_index - 1] + graph[arr[cur_index]]:
                if 0 <= nxt_index < n and nxt_index not in visited:
                    queue.append((nxt_index, step + 1))
                    visited.add(nxt_index)


class Solution2:  # fast
    def minJumps(self, arr: List[int]) -> int:
        # build graph --> {val: inddex}
        n = len(arr)
        graph = collections.defaultdict(list)

        for i, num in enumerate(arr):
            graph[num].append(i)

        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        visited.add(0)
        visitedgroup = set()  # if it's same value, do not need to jump to the position again --> pruning

        while queue:
            cur_index, step = queue.popleft()

            if cur_index == n - 1:
                return step

            for nxt_index in (cur_index + 1), (cur_index - 1):
                if 0 <= nxt_index < n and nxt_index not in visited:
                    queue.append((nxt_index, step + 1))
                    visited.add(nxt_index)

            if arr[cur_index] not in visitedgroup:
                for nxt_index in graph[arr[cur_index]]:
                    if nxt_index not in visited:
                        queue.append((nxt_index, step + 1))
                        visited.add(nxt_index)
                visitedgroup.add(arr[cur_index])


class Solution:  # delete same value from graph to avoid double calculating
    def minJumps(self, arr: List[int]) -> int:
        # build graph --> {val: inddex}
        n = len(arr)
        graph = collections.defaultdict(list)

        for i, num in enumerate(arr):
            graph[num].append(i)

        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        visited.add(0)

        while queue:
            cur_index, step = queue.popleft()

            if cur_index == n - 1:
                return step

            for nxt_index in [cur_index + 1, cur_index - 1] + graph[arr[cur_index]]:
                if 0 <= nxt_index < n and nxt_index not in visited:
                    queue.append((nxt_index, step + 1))
                    visited.add(nxt_index)
            graph.pop(arr[cur_index])  # 剪枝--> 去掉相同 value的position，避免下一次loop