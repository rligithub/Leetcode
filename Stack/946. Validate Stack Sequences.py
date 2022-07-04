class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # push num from pushed, and check if is num in stack[-1] matched to num in popped, if yes, pop

        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while i < len(popped) and stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return len(stack) == 0