class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # build graph --> {bus_stop: bus_id}

        valid = False
        bus = collections.defaultdict(list)
        for i, stops in enumerate(routes):
            for stop in stops:
                if stop == target:
                    valid = True
                bus[stop].append(i)
        if not valid:
            return -1

        queue = collections.deque()
        queue.append((source, 0))
        visited = set()
        visited.add(source)

        while queue:
            cur_stop, count = queue.popleft()

            if cur_stop == target:
                return count

            for nxt_bus in bus[cur_stop]:
                for nxt_stop in routes[nxt_bus]:
                    if nxt_stop not in visited:
                        queue.append((nxt_stop, count + 1))
                        visited.add(nxt_stop)
        return -1


