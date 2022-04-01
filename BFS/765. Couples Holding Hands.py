class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        # build graph {person, seats}-- >  where does he/she sit
        ppl2seat = {}
        for i, ppl in enumerate(row):
            seat = i // 2
            ppl2seat[ppl] = seat

        print(ppl2seat)

        # build graph {seats: u, v} --> couples in the seats
        couch = collections.defaultdict(list)
        for i, ppl in enumerate(row):
            if ppl % 2 == 1:
                couple = ppl - 1
            else:
                couple = ppl + 1

            u = i // 2  # your seat
            v = ppl2seat[couple]  # your couple seat

            if v not in couch[u]:
                couch[u].append(v)
            if u not in couch[v]:
                couch[v].append(u)
        print(couch)
        visited = set()
        count = 0
        for seat in couch.keys():
            if seat not in visited:
                count += 1
                self.bfs(couch, seat, visited)
        return n // 2 - count

    def bfs(self, couch, seat, visited):
        queue = collections.deque()
        queue.append(seat)
        visited.add(seat)
        while queue:
            curseat = queue.popleft()
            for nei in couch[curseat]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
