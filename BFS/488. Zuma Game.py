class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = "".join(sorted(hand))

        q = collections.deque([(board, hand, 0)])
        visited = set([(board, hand)])

        while q:
            curr_board, curr_hand, step = q.popleft()
            for i in range(len(curr_board) + 1):
                for j in range(len(curr_hand)):
                    pick = False
                    if i < len(curr_board) and curr_board[i] == curr_hand[j]:  # 和手上的ball颜色一样
                        pick = True
                    if 0 < i < len(curr_board) and curr_board[i - 1] == curr_board[i] and curr_board[i] != curr_hand[
                        j]:  # 前面两个ball一样但和手上的ball不一样
                        pick = True

                    if pick:
                        new_board = self.remove_same(curr_board[:i] + curr_hand[j] + curr_board[i:])
                        new_hand = curr_hand[:j] + curr_hand[j + 1:]
                        if not new_board:
                            return step + 1
                        if (new_board, new_hand) not in visited:
                            q.append((new_board, new_hand, step + 1))
                            visited.add((new_board, new_hand))

        return -1

    def remove_same(self, s):
        l = r = 0
        while l < len(s):
            while r < len(s) and s[r] == s[l]:
                r += 1
            if r - l > 2:
                return self.remove_same(s[:l] + s[r:])
            l = r
        return s