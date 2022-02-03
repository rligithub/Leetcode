class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # either add full cup or empty cup
        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        visited = set()
        return self.dfs(0, jug1Capacity, jug2Capacity, targetCapacity, visited)

    def dfs(self, cur, cup1, cup2, target, visited):
        visited.add(cur)
        if cur == target:
            return True
        for do in (cup1, -cup1, cup2, -cup2):
            nxt = cur + do
            if nxt not in visited and 0 <= nxt <= cup1 + cup2:
                if self.dfs(nxt, cup1, cup2, target, visited):
                    return True


