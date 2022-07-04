class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # same to #316 only keep unique char to make it smallest

        count = {}
        for i, ch in enumerate(s):
            count[ch] = i

        stack = []
        seen = set()
        for i, ch in enumerate(s):
            if ch in seen:
                continue

            while stack and stack[-1] > ch and i < count[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)