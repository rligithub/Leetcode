class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        queue = collections.deque()
        queue.append(0)
        visited = set()
        visited.add(0)

        while queue:
            cur = queue.popleft()

            for nei in rooms[cur]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return len(visited) == n