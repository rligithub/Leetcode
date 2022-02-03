class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 从每个房间拿到下一个房间的钥匙，求是否能visit完所有房间。初始值 --> 只有第0个房间没上锁
        n = len(rooms)

        visited = set()
        self.dfs(rooms, 0, visited)
        if len(visited) == n:
            return True
        return False

    def dfs(self, rooms, i, visited):
        visited.add(i)
        for nei in rooms[i]:
            if nei not in visited:
                self.dfs(rooms, nei, visited)

