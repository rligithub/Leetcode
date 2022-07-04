class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []  # save ID in stack
        prev_time = 0    # prev time

        for log in logs:
            ID, typ, time = log.split(':')  # "id, type, time"
            ID, time = int(ID), int(time)

            if typ == 'start':
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(ID)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return res