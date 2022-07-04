class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 注意 只能删 重复的char --> 只有后面还会有重复char出现的情况下，才能删除当前的char

        count = {}
        for i, char in enumerate(s):
            count[char] = i

        seen = set()
        stack = []
        for i, char in enumerate(s):
            if char in seen:
                continue
            while stack and stack[-1] > char and i < count[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return "".join(stack)

