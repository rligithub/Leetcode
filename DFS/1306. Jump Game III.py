class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # 每次可以跳 i + arr[i] 或者 i + arr[i]步，求是否能跳到 val为 0的位置 --> 用visited去重（原先跳过的位置 会是一样的结果）
        visited = set()
        return self.dfs(arr, start, visited)

    def dfs(self, arr, pos, visited):
        if pos in visited:
            return False

        if arr[pos] == 0:
            return True
        visited.add(pos)
        for nxt_pos in (pos + arr[pos]), (pos - arr[pos]):
            if 0 <= nxt_pos < len(arr):
                if self.dfs(arr, nxt_pos, visited):
                    return True
        return False